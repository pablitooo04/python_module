try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("pydantic module not found!")
    exit(1)

from enum import Enum
from datetime import datetime
from typing import List


class Rank(str, Enum):
    """Enum for crew member ranks. """
    CADET = "cadet"
    OFFICER = "officer"
    CAPTAIN = "captain"
    COMMANDER = "commander"
    LIEUTENANT = "lieutenant"


class CrewMember(BaseModel):
    """Model for a crew member with validation rules. """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Model for a space mission with complex validation rules. """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_launch_date(self) -> "SpaceMission":
        """
        Custom validation for launch date and mission rules.
        - mission_id must start with 'M'
        - must have at least one Commander or Captain
        - long missions (> 365 days) need at least 50% experienced crew
          (5 + years)
        - all crew members must be active
        """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN]
            for member in self.crew
        ):
            raise ValueError("Mission must have at least one\
                              Commander or Captain")
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5)
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need at \
                        least 50% experienced crew (5+ years)")
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date='2025-07-01',
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=8
                )
            ]
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
    else:
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})", end="")
            print(f" - {member.specialization}")
    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_id="M2024_VENUS",
            mission_name="Venus Atmospheric Study",
            destination="Venus",
            launch_date='2025-08-01',
            duration_days=300,
            budget_millions=1500.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Bob Brown",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Science",
                    years_experience=3
                ),
                CrewMember(
                    member_id="C005",
                    name="Eve Davis",
                    rank=Rank.LIEUTENANT,
                    age=32,
                    specialization="Engineering",
                    years_experience=4
                )
            ]
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
    else:
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value})", end="")
            print(f"- {member.specialization}")


if __name__ == "__main__":
    main()
