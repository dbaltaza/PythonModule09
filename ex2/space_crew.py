from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        leadership_ranks = {Rank.COMMANDER, Rank.CAPTAIN}
        has_leader = any(
            member.rank in leadership_ranks for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            experienced_crew = sum(
                member.years_experience >= 5 for member in self.crew
            )
            if experienced_crew < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    "crew (5+ years)"
                )

        return self


def main() -> None:
    separator = "=" * 41
    print("Space Mission Crew Validation")
    print(separator)

    valid_mission = SpaceMission(
        mission_id="M2026_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-09-01T08:00:00",
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=42,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=31,
                specialization="Engineering",
                years_experience=6,
            ),
        ],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - "
            f"{member.specialization}"
        )
    print(separator)

    try:
        SpaceMission(
            mission_id="M2026_FAIL",
            mission_name="Europa Survey",
            destination="Europa",
            launch_date=datetime(2026, 11, 12, 14, 0, 0),
            duration_days=180,
            crew=[
                CrewMember(
                    member_id="E01",
                    name="Maya Chen",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Science",
                    years_experience=4,
                ),
                CrewMember(
                    member_id="E02",
                    name="Leo Park",
                    rank=Rank.LIEUTENANT,
                    age=33,
                    specialization="Piloting",
                    years_experience=7,
                ),
            ],
            budget_millions=850.0,
        )
    except ValidationError as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
