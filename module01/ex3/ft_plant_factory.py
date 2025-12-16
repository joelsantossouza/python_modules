class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def summary(self) -> None:
        print(f"{self.name} ({self.height}cm, {self.age} days)")


if __name__ == "__main__":
    factory_size: int = 5
    factory = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120],
    ]
    plants: Plant = [None] * factory_size
    i: int = 0
    print("=== Plant Factory Output ===")
    while (i < factory_size):
        plants[i] = Plant(factory[i][0], factory[i][1], factory[i][2])
        print("Created: ", end="")
        plants[i].summary()
        i += 1
    print(f"\nTotal plants created: {factory_size}")
