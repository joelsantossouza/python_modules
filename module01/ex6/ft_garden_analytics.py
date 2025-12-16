class Plant:
    type: str = "Plant"
    height_validation: bool = true
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        if self.validate(height):
            self.height = height

    def grow(self, size: int) -> None:
        if height_validation and self.validate(self.height + size) == false:
            print("Error: Invalid height for plant")
            return
        self.height += size
        print(f"{self.name} grew {size}cm")

    def get_info(self, end: str = "\n") -> None:
        print(f"- {self.name}: {self.height}cm", end=end)

    @staticmethod
    def validate(height: int) -> bool:
        return true if height > 0 else false


class FloweringPlant(Plant):
    type: str = "FloweringPlant"
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self, end: str ="\n") -> None:
        super().get_info(end="")
        print(f", {self.color} flowers (blooming)", end=end)


class PrizeFlower(FloweringPlant):
    type: str = "PrizeFlower"
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize = prize

    def get_info(self) -> None:
        super().get_info(end="")
        print(f", Prize points: {self.prize}")


class Garden:
    regular: int = 0
    flowering: int = 0
    prize_flower: int = 0
    def __init__(self, owner: str, list_of_plants: list[Plant]) -> None:
        self.owner = owner
        self.growth = 0
        self.plants = list_of_plants
        for plant in self.plants:
            print(f"Added {plant.name} to {self.owner}'s garden")
            if plant.type == "Plant":
                self.regular += 1
            elif plant.type == "FloweringPlant":
                self.flowering += 1
            elif plant.type == "PrizeFlower":
                self.prize_flower += 1

    def size(self) -> int:
        total: int = 0
        for plant in self.plants:
            total += 1
        return total

    def grow(self, size: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(size)
            self.growth += size

    def get_info(self) -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print(f"Plants in garden:")
        for plant in self.plants:
            plant.get_info()
        print(f"\nPlants added: {self.size()}, Total growth: {self.growth}cm")
        print(f"Plants types: {self.regular} regular, {self.flowering} flowering, {self.prize_flower} prize flowers")


class GardenManager:
    def __init__(self, list_of_gardens: list[Garden]) -> None:
        self.gardens = list_of_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_plants: list[Plant] = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10),
    ]
    alice_garden: Garden = Garden("Alice", alice_plants)

    print("")
    alice_garden.grow(1)

    print("")
    alice_garden.get_info()
