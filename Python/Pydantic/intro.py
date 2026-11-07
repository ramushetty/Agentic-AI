# Pydantic help in type validation
# also helps with field validation
# data validation


from pydantic import BaseModel, ValidationError

class SignUpForm(BaseModel):
    username: str
    email: str
    age: int
    newsletter_opt_in: bool = False  # has a default --> OPTIONAL field


incoming_Data = {"username":"ramu","email":"ramu@gmail.com","age":28}

user_a = SignUpForm(**incoming_Data)  # dictionary unpacking
# which allows you to dynamically convert key-value pairs from a dictionary into keyword arguments (kwargs)

# Pydantic does little bit of automatic type coerction
# like {"age" : "28"}  it automatically converts to int , bool for boolean case

# "28" ------> 28
# "twenty-eight" -----> validationError
# "True" ------> True 
# "28.5" -----> error




from typing import Annotated
from pydantic import BaseModel, Field

# Field and annotated both are same nothing different

# Direct style
class JobApplicationV1(BaseModel):
    full_name: str = Field(min_length=2, max_length=100)
    years_experience: int = Field(ge=0, le=50)
    portfolio_url: str = Field(pattern=r"^https?://.*")

# Annotated style — same behavior, more composable
class JobApplicationV2(BaseModel):
    full_name: Annotated[str, Field(min_length=2, max_length=100)]
    years_experience: Annotated[int, Field(ge=0, le=50)]
    email: Annotated[
        str,
        Field(description="Applicant's contact email", examples=["rohan@example.com"]),
    ]



# build in special types 

from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr

class Applicant(BaseModel):
    name: str
    email: EmailStr        # rejects "not-an-email"
    website: HttpUrl        # must be http:// or https://

class UserAccount(BaseModel):
    username: str
    password: SecretStr

account = UserAccount(username="rohan99", password="super-secret-123")
print(account)                              # password shows as **********
print(account.password.get_secret_value())  # the real value, on purpose









