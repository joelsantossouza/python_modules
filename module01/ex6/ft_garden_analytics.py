class Plant:
    type: str = "Plant"
    height_validation: bool = True

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        if self.validate(height):
            self.height = height

    def grow(self, size: int) -> None:
        if self.height_validation and not self.validate(self.height + size):
            print("Error: Invalid height for plant")
            return
        self.height += size
        print(f"{self.name} grew {size}cm")

    def get_info(self, end: str = "\n") -> None:
        print(f"- {self.name}: {self.height}cm", end=end)

    @staticmethod
    def validate(height: int) -> bool:
        return True if height > 0 else False

    @classmethod
    def toggle_height_validation(cls) -> None:
        if cls.height_validation:
            cls.height_validation = False
        else:
            cls.height_validation = True


class FloweringPlant(Plant):
    type: str = "FloweringPlant"

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self, end: str = "\n") -> None:
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
    growth: int = 0

    def __init__(self, owner: str, list_of_plants: list[Plant]) -> None:
        self.owner = owner
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
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()
        print(
            f"\nPlants added: {self.size()}, "
            f"Total growth: {self.growth}cm"
        )
        print(
            "Plants types: "
            f"{self.regular} regular, "
            f"{self.flowering} flowering, "
            f"{self.prize_flower} prize flowers"
        )


class GardenManager:
    class GardenStats:
        @staticmethod
        def score(garden: Garden) -> int:
            points: int = 0
            for plant in garden.plants:
                points += plant.height
                if plant.type == "PrizeFlower":
                    points += plant.prize
            return points

    def __init__(self, list_of_gardens: list[Garden]) -> None:
        self.gardens = list_of_gardens
        self.stats = self.GardenStats()

    def create_garden_network(self, list_of_gardens: list[Garden]) -> None:
        self.gardens = list_of_gardens

    def number_of_gardens(self) -> int:
        ngardens: int = 0
        for garden in self.gardens:
            ngardens += 1
        return ngardens

    def get_info(self) -> None:
        print(f"Height validation test: {Plant.height_validation}")
        print("Garden scores:")
        for garden in self.gardens:
            print(f"- {garden.owner} -> {self.stats.score(garden)} points")
        print(f"\nTotal gardens managed: {self.number_of_gardens()}")


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

    print("\n---------------")
    bob_plants: list[Plant] = [
        Plant("Pine", 80),
        FloweringPlant("tulips", 15, "blue"),
    ]
    bob_garden: Garden = Garden("Bob", bob_plants)

    print("")
    bob_garden.grow(3)

    print("")
    bob_garden.get_info()

    print("\n---------------")
    manager: GardenManager = GardenManager([alice_garden, bob_garden])
    manager.get_info()
