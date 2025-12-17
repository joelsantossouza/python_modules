def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Check if the plant status has valid data (name, water, sunlight)
    """
    try:
        if plant_name is None:
            raise ValueError("Plant name cannot be empty!")
        if water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        elif sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)"
            )
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks() -> None:
    """
    Test each plant health case
    """
    good_values = [
        ["Tomato", 10, 12],
        ["Carrot", 1, 2],
        ["Lettuce", 5, 6],
    ]
    print("\nTesting good values...")
    for value in good_values:
        check_plant_health(value[0], value[1], value[2])

    print("\nTesting empty plant name...")
    check_plant_health(None, 5, 5)

    print("\nTesting bad water level...")
    check_plant_health("Apple", 0, 5)
    check_plant_health("Watermelon", 100, 5)

    print("\nTesting bad sunlight hours...")
    check_plant_health("Apple", 5, 0)
    check_plant_health("Watermelon", 5, 20)


# if __name__ == "__main__":
#     print("=== Garden Plant Health Checker ===")
#     test_plant_checks()
#     print("\nAll errors raising tests completed!")
