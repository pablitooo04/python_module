try:
    from pydantic import BaseModel, ValidationError, Field
except ImportError:
    print("pydantic module not found !")
    exit(1)
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="1998-01-01"
        )
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"])
        exit(1)

    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:",
          "Operational" if station.is_operational else "Not Operational")
    print(station.last_maintenance)
    print()

    print("========================================")

    try:
        print("Expected validation error:")
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=100,
            power_level=85.5,
            oxygen_level=80.80,
            last_maintenance="1998-01-01"
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
