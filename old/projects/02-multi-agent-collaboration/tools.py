"""The "business" side of the refund desk: a tiny fake shop database and four tools.

These are plain Python functions. They know nothing about agents or LLMs.
The governance layer (governance.py) decides WHO may call them.
"""

REFUND_WINDOW_DAYS = 30  # refunds are allowed for 30 days after delivery
APPROVAL_LIMIT = 100.0   # refunds above this amount need a human to approve

ORDERS = {
    "A100": {"customer": "Raj", "item": "Headphones", "amount": 40.0, "delivered": True, "days_since_delivery": 5},
    "A200": {"customer": "Sam", "item": "Laptop", "amount": 900.0, "delivered": True, "days_since_delivery": 10},
    "A300": {"customer": "Priya", "item": "Shoes", "amount": 60.0, "delivered": True, "days_since_delivery": 90},
    "A500": {"customer": "Lee", "item": "Backpack", "amount": 55.0, "delivered": True, "days_since_delivery": 3},
}

REFUNDS_ISSUED = {}   # order_id -> refund record (our fake payment system)
_LOOKUP_CALLS = {}    # counts calls per order, so A500 can fail twice like a flaky service


def reset_fake_world():
    """Forget all refunds and flaky-call counts. Used by the demo and the tests."""
    REFUNDS_ISSUED.clear()
    _LOOKUP_CALLS.clear()


def get_order(order_id):
    """Read-only. Order A500 times out on its first 2 calls, to show retries."""
    _LOOKUP_CALLS[order_id] = _LOOKUP_CALLS.get(order_id, 0) + 1
    if order_id == "A500" and _LOOKUP_CALLS[order_id] <= 2:
        raise TimeoutError("order service timed out")
    if order_id not in ORDERS:
        return {"found": False, "order_id": order_id}
    return {"found": True, "order_id": order_id, **ORDERS[order_id]}


def check_refund_policy(order):
    """Read-only. Applies the shop's rules to one order."""
    if not order["delivered"]:
        return {"eligible": False, "needs_approval": False, "reason": "order was not delivered yet"}
    if order["days_since_delivery"] > REFUND_WINDOW_DAYS:
        reason = f"delivered {order['days_since_delivery']} days ago, window is {REFUND_WINDOW_DAYS} days"
        return {"eligible": False, "needs_approval": False, "reason": reason}
    needs_approval = order["amount"] > APPROVAL_LIMIT
    return {"eligible": True, "needs_approval": needs_approval, "reason": "inside the refund window"}


def issue_refund(order_id, amount, approved_by=None):
    """The ONLY tool that moves money.

    It protects itself: a big refund without an approver is refused HERE, even if the graph
    had a bug. It is also idempotent: asking twice for the same order refunds once.
    """
    if amount > APPROVAL_LIMIT and not approved_by:
        raise PermissionError(f"refund of {amount} needs a human approver")
    if order_id in REFUNDS_ISSUED:
        return {**REFUNDS_ISSUED[order_id], "duplicate": True}
    REFUNDS_ISSUED[order_id] = {"order_id": order_id, "amount": amount, "approved_by": approved_by, "duplicate": False}
    return REFUNDS_ISSUED[order_id]


def delete_customer(customer):
    """A dangerous tool that exists in the company but is on NO worker's allowlist."""
    return {"deleted": customer}


TOOLS = {
    "get_order": get_order,
    "check_refund_policy": check_refund_policy,
    "issue_refund": issue_refund,
    "delete_customer": delete_customer,
}
