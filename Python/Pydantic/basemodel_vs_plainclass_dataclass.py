from dataclasses import dataclass
from pydantic import BaseModel

# Option 1: dataclass — clean syntax, ZERO validation
@dataclass
class UserDataclass:
    name: str
    email: str
    age: int

user = UserDataclass(name="Alice", email="alice@example.com", age="not a number")
print(user.age)   # "not a number" — accepted with no complaint at all

# Option 2: BaseModel — actually inspects the data
class UserModel(BaseModel):
    name: str
    email: str
    age: int

UserModel(name="Alice", email="alice@example.com", age="not a number")
# ValidationError: Input should be a valid integer,
# unable to parse string as an integer

# But a numeric STRING is coerced safely:
user = UserModel(name="Alice", email="alice@example.com", age="30")
print(user.age, type(user.age))   # 30 <class 'int'>



user.model_dump()