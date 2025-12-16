class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, size: int) -> None:
        self.height += size
        print(f"{self.name} grew {size}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize: int) -> None:
        super().__init__(name, height, age, color)
        self.prize = prize


class Garden:
    def __init__(self, owner: str, list_of_plants: Plant[]) -> None:
        self.owner = owner
        self.plants = list_of_plants
        for plant in self.plants:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow(self, size: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(size)

    def get_info(self) -> None:
        print(f"Plants in {self.owner}'s garden:")
        for plant in self.plants:


class GardenManager:
    def __init__(self, list_of_gardens: Garden[]) -> None:
        self.gardens = list_of_gardens

    class GardenStats:
