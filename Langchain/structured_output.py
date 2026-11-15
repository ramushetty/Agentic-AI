def create_agent(
    ...
    response_format: Union[
        ToolStrategy[StructuredResponseT],
        ProviderStrategy[StructuredResponseT],
        type[StructuredResponseT],
        None,
    ]
)



# Response format
# Use response_format to control how the agent returns structured data:
# ToolStrategy[StructuredResponseT]: Uses tool calling for structured output
# ProviderStrategy[StructuredResponseT]: Uses provider-native structured output
# type[StructuredResponseT]: Schema type - automatically selects best strategy based on model capabilities
# None: Structured output not explicitly requested


# Provider strategy

class ProviderStrategy(Generic[SchemaT]):
    schema: type[SchemaT]
    strict: bool | None = None



from pydantic import BaseModel, Field
from langchain.agents import create_agent


class ContactInfo(BaseModel):
    """Contact information for a person."""
    name: str = Field(description="The name of the person")
    email: str = Field(description="The email address of the person")
    phone: str = Field(description="The phone number of the person")

agent = create_agent(
    model="gpt-6.1-sol",
    response_format=ContactInfo  # Auto-selects ProviderStrategy
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

print(result["structured_response"])
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')



# Tool calling strategy
# For models that don’t support native structured output, LangChain uses tool calling to achieve the same result. This works with all models that support tool calling (most modern models).


from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


class ProductReview(BaseModel):
    """Analysis of a product review."""
    rating: int | None = Field(description="The rating of the product", ge=1, le=5)
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the review")
    key_points: list[str] = Field(description="The key points of the review. Lowercase, 1-3 words each.")

agent = create_agent(
    model="gpt-6.1-sol",
    tools=[],
    response_format=ToolStrategy(ProductReview)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Analyze this review: 'Great product: 5 out of 5 stars. Fast shipping, but expensive'"}]
})
result["structured_response"]
# ProductReview(rating=5, sentiment='positive', key_points=['fast shipping', 'expensive'])


# Custom tool message content

from pydantic import BaseModel, Field
from typing import Literal
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


class MeetingAction(BaseModel):
    """Action items extracted from a meeting transcript."""
    task: str = Field(description="The specific task to be completed")
    assignee: str = Field(description="Person responsible for the task")
    priority: Literal["low", "medium", "high"] = Field(description="Priority level")

agent = create_agent(
    model="gpt-6.1-sol",
    tools=[],
    response_format=ToolStrategy(
        schema=MeetingAction,
        tool_message_content="Action item captured and added to meeting notes!"
    )
)

agent.invoke({
    "messages": [{"role": "user", "content": "From our meeting: Sarah needs to update the project timeline as soon as possible"}]
})

# ================================ Human Message =================================

# From our meeting: Sarah needs to update the project timeline as soon as possible
# ================================== Ai Message ==================================
# Tool Calls:
#   MeetingAction (call_1)
#  Call ID: call_1
#   Args:
#     task: Update the project timeline
#     assignee: Sarah
#     priority: high
# ================================= Tool Message =================================
# Name: MeetingAction

# Action item captured and added to meeting notes!




# Error handling

# Multiple structured outputs error

from pydantic import BaseModel, Field
from typing import Union
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


class ContactInfo(BaseModel):
    name: str = Field(description="Person's name")
    email: str = Field(description="Email address")

class EventDetails(BaseModel):
    event_name: str = Field(description="Name of the event")
    date: str = Field(description="Event date")

agent = create_agent(
    model="gpt-6.1-sol",
    tools=[],
    response_format=ToolStrategy(Union[ContactInfo, EventDetails])  # Default: handle_errors=True
)

agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})

# ================================ Human Message =================================

# Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th
# None
# ================================== Ai Message ==================================
# Tool Calls:
#   ContactInfo (call_1)
#  Call ID: call_1
#   Args:
#     name: John Doe
#     email: john@email.com
#   EventDetails (call_2)
#  Call ID: call_2
#   Args:
#     event_name: Tech Conference
#     date: March 15th
# ================================= Tool Message =================================
# Name: ContactInfo

# Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
#  Please fix your mistakes.
# ================================= Tool Message =================================
# Name: EventDetails

# Error: Model incorrectly returned multiple structured responses (ContactInfo, EventDetails) when only one is expected.
#  Please fix your mistakes.
# ================================== Ai Message ==================================
# Tool Calls:
#   ContactInfo (call_3)
#  Call ID: call_3
#   Args:
#     name: John Doe
#     email: john@email.com
# ================================= Tool Message =================================
# Name: ContactInfo

# Returning structured response: {'name': 'John Doe', 'email': 'john@email.com'}



# Schema validation error

from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy


class ProductRating(BaseModel):
    rating: int | None = Field(description="Rating from 1-5", ge=1, le=5)
    comment: str = Field(description="Review comment")

agent = create_agent(
    model="gpt-6.1-sol",
    tools=[],
    response_format=ToolStrategy(ProductRating),  # Default: handle_errors=True
    system_prompt="You are a helpful assistant that parses product reviews. Do not make any field or value up."
)

agent.invoke({
    "messages": [{"role": "user", "content": "Parse this: Amazing product, 10/10!"}]
})


# ================================ Human Message =================================

# Parse this: Amazing product, 10/10!
# ================================== Ai Message ==================================
# Tool Calls:
#   ProductRating (call_1)
#  Call ID: call_1
#   Args:
#     rating: 10
#     comment: Amazing product
# ================================= Tool Message =================================
# Name: ProductRating

# Error: Failed to parse structured output for tool 'ProductRating': 1 validation error for ProductRating.rating
#   Input should be less than or equal to 5 [type=less_than_equal, input_value=10, input_type=int].
#  Please fix your mistakes.
# ================================== Ai Message ==================================
# Tool Calls:
#   ProductRating (call_2)
#  Call ID: call_2
#   Args:
#     rating: 5
#     comment: Amazing product
# ================================= Tool Message =================================
# Name: ProductRating

# Returning structured response: {'rating': 5, 'comment': 'Amazing product'}


# Custom error handler function:

from langchain.agents.structured_output import StructuredOutputValidationError
from langchain.agents.structured_output import MultipleStructuredOutputsError

def custom_error_handler(error: Exception) -> str:
    if isinstance(error, StructuredOutputValidationError):
        return "There was an issue with the format. Try again."
    elif isinstance(error, MultipleStructuredOutputsError):
        return "Multiple structured outputs were returned. Pick the most relevant one."
    else:
        return f"Error: {str(error)}"


agent = create_agent(
    model="gpt-6.1-sol",
    tools=[],
    response_format=ToolStrategy(
                        schema=Union[ContactInfo, EventDetails],
                        handle_errors=custom_error_handler
                    )  # Default: handle_errors=True
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract info: John Doe (john@email.com) is organizing Tech Conference on March 15th"}]
})

for msg in result['messages']:
    # If message is actually a ToolMessage object (not a dict), check its class name
    if type(msg).__name__ == "ToolMessage":
        print(msg.content)
    # If message is a dictionary or you want a fallback
    elif isinstance(msg, dict) and msg.get('tool_call_id'):
        print(msg['content'])