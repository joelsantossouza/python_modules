class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        print("Leaving the land very dry")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        print("Wasting a lot of water from the tank")
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def test_garden_error() -> None:
    print("Testing GardenError...")
    try:
        print("Leaving the land very dry")
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print()
    try:
        print("Wasting a lot of water from the tank")
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


# if __name__ == "__main__":
#     print("=== Custom Garden Errors Demo ===")
#     test_plant_error()
#     print()
#     test_water_error()
#     print()
#     test_garden_error()
