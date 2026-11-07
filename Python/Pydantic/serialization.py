# user = SignupForm(username="aditi28", email="aditi@example.com", age=28, newsletter_opt_in=True)

# user.model_dump()
# # {'username': 'aditi28', 'email': 'aditi@example.com', 'age': 28, 'newsletter_opt_in': True}

# user.model_dump_json()
# # '{"username":"aditi28","email":"aditi@example.com","age":28,"newsletter_opt_in":true}'

# user.model_dump_json(indent=2)   # pretty-printed for humans/logs