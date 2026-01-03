from pydantic import BaseModel, Field, model_validator
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
        if self.mission_id[:1] != "M":
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
                "For long missions (>365) 50% of crew "
                "must have 5+ years of experience"
            )
        return self


def main() -> None:
    """Main function"""
    print("Space Mission Crew Validation")
    crew_valid: list[CrewMember] = [
        CrewMember(
            member_id="C01",
            name="Sarah Connor",
            rank="commander",
            age=45,
            specialization="Mission Command",
            years_experience=15,
            is_active=True
        ),
        CrewMember(
            member_id="C02",
            name="John Smith",
            rank="lieutenant",
            age=38,
            specialization="Navigation",
            years_experience=6,
            is_active=True
        ),
        CrewMember(
            member_id="C03",
            name="Alice Johnson",
            rank="officer",
            age=32,
            specialization="Engineering",
            years_experience=3,
            is_active=True
        ),
    ]

    crew_invalid_no_leader: list[CrewMember] = [
        CrewMember(
            member_id="C04",
            name="Bob Lee",
            rank="lieutenant",
            age=40,
            specialization="Science",
            years_experience=10,
            is_active=True
        )
    ]

    crew_invalid_experience: list[CrewMember] = [
        CrewMember(
            member_id="C05",
            name="Tom Rookie",
            rank="captain",
            age=35,
            specialization="Command",
            years_experience=2,
            is_active=True
        ),
        CrewMember(
            member_id="C06",
            name="Jane Rookie",
            rank="officer",
            age=29,
            specialization="Engineering",
            years_experience=1,
            is_active=True
        )
    ]

    crew_inactive: list[CrewMember] = [
        CrewMember(
            member_id="C07",
            name="Mark Oldman",
            rank="commander",
            age=60,
            specialization="Strategy",
            years_experience=30,
            is_active=False
        )
    ]

    inputs: list[dict] = [
        # ✅ VALID MISSION
        {
            "mission_id": "M2024_MARS",
            "mission_name": "Mars Colony Establishment",
            "destination": "Mars",
            "launch_date": "2025-12-31",
            "duration_days": 900,
            "crew": crew_valid,
            "mission_status": "planned",
            "budget_millions": 2500.0,
        },

        # ❌ No Commander or Captain
        {
            "mission_id": "M2025_MOON",
            "mission_name": "Moon Research",
            "destination": "Moon",
            "launch_date": "2025-06-01",
            "duration_days": 200,
            "crew": crew_invalid_no_leader,
            "mission_status": "planned",
            "budget_millions": 500.0,
        },

        # ❌ Long mission, not enough experienced crew
        {
            "mission_id": "M2026_JUP",
            "mission_name": "Jupiter Deep Scan",
            "destination": "Jupiter",
            "launch_date": "2026-01-01",
            "duration_days": 800,
            "crew": crew_invalid_experience,
            "mission_status": "planned",
            "budget_millions": 4000.0,
        },

        # ❌ Inactive crew member
        {
            "mission_id": "M2027_AST",
            "mission_name": "Asteroid Mining",
            "destination": "Asteroid Belt",
            "launch_date": "2027-03-10",
            "duration_days": 300,
            "crew": crew_inactive,
            "mission_status": "planned",
            "budget_millions": 1500.0,
        },
    ]
    for i, input in enumerate(inputs):
        print("======================================")
        print(f"Test {i + 1}:")
        try:
            result: SpaceMission = SpaceMission(
                mission_id=input["mission_id"],
                mission_name=input["mission_name"],
                destination=input["destination"],
                launch_date=input["launch_date"],
                duration_days=input["duration_days"],
                crew=input["crew"],
                mission_status=input["mission_status"],
                budget_millions=input["budget_millions"]
            )
            for key, value in result.model_dump().items():
                if key == "crew":
                    print("crew:")
                    for member in value:
                        print(f" - {member['name']} ({member['rank']})")
                else:
                    print(f"{key}: {value}")
        except Exception as e:
            print("ERRORS: ", end="")
            for error in e.errors():
                print(error['msg'], end=", ")
            print()


if __name__ == "__main__":
    main()
