class   Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
    def summary(self) -> None:
        print(f"{self.name} : {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)
    rose.summary()
    sunflower.summary()
    cactus.summary()
