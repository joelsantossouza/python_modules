class GardenError(Exception):
    """
    Geral garden errors
    """
    pass


class PlantError(GardenError):
    """
    Plant's specific errors
    """
    pass


class WaterError(GardenError):
    """
    Water's specific error
    """
    pass


class SunlightError(GardenError):
    """
    Sunlight's specific error
    """
    pass


class GardenManager:
    """
    Manages a list of gardens, that eventually has a list of plants
    """

    def garden_size(self, list_of_plants, check_none: bool = True) -> int:
        size: int = 0
        for plant in list_of_plants:
            if check_none and plant[0] is None:
                break
            size += 1
        return size

    def add_plants(self, list_of_plants) -> None:
        self.plants = [None] * self.garden_size(list_of_plants)
        size: int = self.garden_size(list_of_plants, False)
        i: int = 0
        try:
            while (i < size):
                if list_of_plants[i][0] is None:
                    raise PlantError("Plant name cannot be empty!")
                self.plants[i] = list_of_plants[i]
                print(f"Added {list_of_plants[i][0]} successfully")
                i += 1
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise PlantError("Plant name cannot be empty!")
                print(f"Watering {plant[0]} - success")
        except PlantError as e:
            print(f"Error watering plant: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.plants:
            try:
                if plant[1] < 1:
                    raise WaterError(
                        f"Water level {plant[1]} is too low (min 1)"
                    )
                elif plant[1] > 10:
                    raise WaterError(
                        f"Water level {plant[1]} is too high (max 10)"
                    )
                if plant[2] < 2:
                    raise SunlightError(
                        f"Sunlight hours {plant[2]} is too low (min 2)"
                    )
                elif plant[2] > 12:
                    raise SunlightError(
                        f"Sunlight hours {plant[2]} is too high (max 12)"
                    )
                print(
                    f"{plant[0]}: healthy (water: {plant[1]}, sun: {plant[2]})"
                )
            except GardenError as e:
                print(f"Error checking {plant[0]}: {e}")

    def recovery(self) -> None:
        print("Wasting a lot of water from the tank")
        try:
            raise WaterError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")


# if __name__ == "__main__":
#     print("=== Garden Management System ===")
#     garden: GardenManager = GardenManager()
#     plants = [
#         ["tomato", 5, 8],
#         ["lettuce", 0, 8],
#         ["apple", 19, 8],
#         ["watermelon", 3, 0],
#         ["carrot", 3, 13],
#         [None, 5, 8],
#     ]
#     print("\nAdding plants to garden...")
#     garden.add_plants(plants)
#
#     print("\nWatering plants...")
#     garden.water_plants()
#
#     print("\nChecking plants health...")
#     garden.check_plant_health()
#
#     print("\nTesting error recovery...")
#     garden.recovery()
#
#     print("\nGarden management system test complete!")
