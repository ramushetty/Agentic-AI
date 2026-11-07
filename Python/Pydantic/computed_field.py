from pydantic import BaseModel, computed_field

class JobApplication(BaseModel):
    full_name: str
    years_experience: int

    @computed_field
    @property
    def experience_tier(self) -> str:
        if self.years_experience < 2:
            return "junior"
        elif self.years_experience < 7:
            return "mid"
        return "senior"

app = JobApplication(full_name="Aditi Sharma", years_experience=6)
print(app.experience_tier)      # "mid" — accessed like a normal attribute
print(app.model_dump())         # includes experience_tier automatically

app.years_experience = 10       # models are mutable by default
print(app.experience_tier)      # "senior" — always fresh, never stale

