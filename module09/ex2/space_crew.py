from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class Rank(Enum):
    """Options of rank to a crew member"""
    cadet: str = "cadet"
    officer: str = "officer"
    lieutenant: str = "lieutenant"
    captain: str = "captain"
    commander: str = "commander"


class CrewMember(BaseModel):
    """Attributes of a crew member"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Attributes and validation of valid mission"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate(self):
        if self.mission_id[:1] == "M":
            raise ValueError(f"{self.mission_id} must start with 'M'")
        has_lider: bool = False
        size: int = 0
        experients: int = 0
        for member in self.crew:
            size += 1
            if not member.is_active:
                raise ValueError(f"Member '{member.name}' is not active")
            if member.rank == Rank.commander or member.rank == Rank.captain:
                has_lider = True
            if member.years_experience >= 5:
                experients += 1
        if not has_lider:
            raise ValueError("Crew must have one commander or captain")
        if self.duration_days > 365 and experients < (size / 2):
            raise ValueError(
                "For long missions (>365) 50% of crew"
                "must have 5+ years of experience"
            )
        return self


if __name__ == "__main__":
