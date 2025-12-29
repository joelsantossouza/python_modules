from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any


class SpaceStation(BaseModel):
    """Data type validation for Space Stations"""
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: Optional[bool] = Field(default=True)
    notes: Optional[str] = Field(default="", max_length=100)


def main() -> None:
    """Main function to test validations"""
    print("Space Station Data Validation")
    print("========================================")
    space_station: SpaceStation = SpaceStation(
        station_id="SS001", name="International Space Station",
        crew_size=6, power_level=85.5, oxygen_level=92.3,
        last_maintenance="2025-12-29"
    )
    print("Valid station created:")
    print(f"ID: {space_station.station_id}")
    print(f"Name: {space_station.name}")
    print(f"Crew: {space_station.crew_size}")
    print(f"Power: {space_station.power_level}")
    print(f"Oxygen: {space_station.oxygen_level}")
    if space_station.is_operational:
        print("Status: Operational")
    else:
        print("Status: Not operational")
    print(f"Notes: {space_station.notes}")

    print("\n\nSpace Station Data Validation - [INVALIDS]")
    print("========================================")
    inputs: list[list[Any]] = [
        ["123", "Test", 6, 85.5, 92.3, "2025-12-29", True, ""],
        [1, "Test", 6, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", 1, 6, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", [0, 1], 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6.1, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6, "hey", 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6, 85.5, "hey", "2025-12-29", True, ""],
        ["123", "Test", 6, 85.5, 92.3, "92j92jf92jf92", True, ""],
        ["123", "Test", 6, 85.5, 92.3, "2025-12-29", 282, ""],
        ["123", "Test", 6, 85.5, 92.3, "2025-12-29", False, 29],
        ["12", "Test", 6, 85.5, 92.3, "2025-12-29", True, ""],
        ["12345678910", "Test", 6, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "", 6, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", -5, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 21, 85.5, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6, -1, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6, 100.1, 92.3, "2025-12-29", True, ""],
        ["123", "Test", 6, 100, -100, "2025-12-29", True, ""],
        ["123", "Test", 6, 100, 200.1, "2025-12-29", True, ""],
    ]
    i: int = 0
    for id, name, crew, power, oxygen, maintenance, is_op, notes in inputs:
        i += 1
        print(f"Test {i}: ", end="")
        try:
            SpaceStation(
                station_id=id, name=name, crew_size=crew, power_level=power,
                oxygen_level=oxygen, last_maintenance=maintenance,
                is_operational=is_op, notes=notes
            )
            print("OK")
        except Exception as e:
            for error in e.errors():
                print(error['msg'], end=", ")
            print()


if __name__ == "__main__":
    main()
