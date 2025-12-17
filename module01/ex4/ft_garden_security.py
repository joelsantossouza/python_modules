class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.set_height(height)
        self.set_age(age)
        self.name = name

    def set_height(self, height: int) -> None:
        if height < 0:
            print("Security: Negative height rejected")
            return
        self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print("Security: Impossible age")
            return
        self.__age = age

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_info(self) -> None:
        print(f"{self.name} ({self.__height}cm, {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: SecurePlant = SecurePlant("Rose", 0, 0)
    print("Plant created: ", end="")
    rose.get_info()
    rose.set_height(25)
    print(f"Height updated: {rose.get_height()}cm [OK]")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days [OK]")

    print("\nTrying to set height to -5...")
    rose.set_height(-5)

    print("\nTrying to set age to -5...")
    rose.set_age(-5)

    print("\nCurrent plant state: ", end="")
    rose.get_info()
