from pydantic import BaseModel, model_validator

class SignupForm(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_must_match(self):
        if self.password != self.confirm_password:
            raise ValueError("password and confirm_password do not match")
        return self

# A richer example — mutually exclusive preferences
class JobApplication(BaseModel):
    remote_preferred: bool
    willing_to_relocate: bool

    @model_validator(mode="after")
    def check_relocation_logic(self):
        if self.remote_preferred and self.willing_to_relocate:
            raise ValueError("Can't be both remote-only AND willing to relocate")
        return self