class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growth(self, size: int) -> None:
        self.height += size

    def aging(self, time: int) -> None:
        self.age += time

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    weeks: int = 1
    day: int = 0
    print(f"=== Day {day} ===")
    rose.get_info()
    while (weeks > 0):
        rose.growth(6)
        rose.aging(7)
        day += 7
        weeks -= 1
        print(f"=== Day {day} ===")
        rose.get_info()
        print("Growth this week: +6cm")
