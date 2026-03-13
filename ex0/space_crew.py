from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceCrew(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    separator = "=" * 40
    print("Space Station Data Validation")
    print(separator)

    try:
        valid_station = SpaceCrew(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 3, 13, 10, 30),
            is_operational=True,
            notes="Primary orbital research station",
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        status = (
            "Operational"
            if valid_station.is_operational
            else "Not Operational"
        )
        print(f"Status: {status}")
    except Exception as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])

    print("\n",separator)

    try:
        SpaceCrew(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 3, 13, 10, 30),
            is_operational=True,
            notes="Primary orbital research station",
        )
    except Exception as error:
        print("Expected validation error:")
        print(error.errors()[0]["msg"])


if __name__ == "__main__":
    main()
