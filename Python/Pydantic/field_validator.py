from pydantic import BaseModel, field_validator

class JobApplication(BaseModel):
    full_name: str
    email: str
    years_experience: int

    @field_validator("full_name", mode="after")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("full_name cannot be empty")
        return cleaned.title()

    @field_validator("years_experience", mode="before")
    @classmethod
    def strip_years_suffix(cls, value):
        # handles messy input like "5 years" arriving as raw text
        if isinstance(value, str):
            digits = "".join(ch for ch in value if ch.isdigit())
            return int(digits) if digits else value
        return value

app = JobApplication(full_name="  rohan mehta  ", email="r@x.com", years_experience="5 years")
print(app.full_name, app.years_experience)   # Rohan Mehta 5
