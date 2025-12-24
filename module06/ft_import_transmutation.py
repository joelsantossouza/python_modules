import alchemy
from alchemy.elements import create_water
from alchemy.potions import healing_potion as heal
from alchemy.elements import create_earth, create_fire
from alchemy.potions import strength_potion

if __name__ == "__main__":
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    fire: str = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire}")

    print("\nMethod 2 - Specific function import:")
    water: str = create_water()
    print(f"create_water(): {water}")

    print("\nMethod 3 - Aliased import:")
    healing: str = heal()
    print(f"heal(): {healing}")

    print("\nMethod 4 - Multiple imports:")
    earth: str = create_earth()
    fire: str = create_fire()
    strength: str = strength_potion()
    print(f"create_earth(): {earth}")
    print(f"create_fire(): {fire}")
    print(f"strength_potion(): {strength}")

    print("\nAll import transmutation methods mastered!")
