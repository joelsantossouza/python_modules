class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self, end: str = "\n") -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days", end=end)


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(self.name + " is blooming beautifully!")

    def get_info(self) -> None:
        print("[Flower] - ", end="")
        super().get_info(end="")
        print(f", {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diameter

    def produce_shade(self) -> None:
        print(
            f"{self.name} provides "
            f"{(self.height * self.diameter) / 100} "
            "square meters of shade"
        )

    def get_info(self) -> None:
        print("[Tree] - ", end="")
        super().get_info(end="")
        print(f", {self.diameter}cm diameter")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutri_info(self) -> None:
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

    def get_info(self) -> None:
        print("[Vegetable] - ", end="")
        super().get_info(end="")
        print(f", {self.harvest_season} harvest")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("\n-- Flowers --")
    rose: Flower = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()
    print("")

    tulips: Flower = Flower("Tulips", 15, 7, "yellow")
    tulips.get_info()
    tulips.bloom()
    print("")

    print("\n-- Trees --")
    oak: Tree = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()
    print("")

    pines: Tree = Tree("Pines", 2500, 36500, 80)
    pines.get_info()
    pines.produce_shade()
    print("")

    print("\n-- Vegetables --")
    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    tomato.get_info()
    tomato.nutri_info()
    print("")

    spinach: Vegetable = Vegetable("Spinach", 20, 80, "spring", "K")
    spinach.get_info()
    spinach.nutri_info()
