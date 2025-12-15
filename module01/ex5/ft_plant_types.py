class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, end: str = "\n") -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days", end=end)


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(self, name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(self.name + " is blooming beautifully!")

    def get_info(self) -> None:
        print("[Flower] - ", end="")
        super().get_info(self, end="")
        print(f", {self.color} color")



class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.height * self.trunk_diameter} square meters of shade")

    def get_info(self) -> None:
        print("[Tree] - ", end="")
        super().get_info(self, end="")
        print(f", {self.trunk_diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutricional_value = nutricional_value

    def nutri_info(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutricional_value}")

    def get_info(self) -> None:
        print("[Vegetable] - ", end="")
        super().get_info(self, end="")
        print(f", {self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose: Flower = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()

    oak: Tree = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer")
    tomato.get_info()
    tomato.nutri_info()
