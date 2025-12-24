from alchemy.grimoire import validate_ingredients, record_spell

if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    validate1: str = validate_ingredients("fire air")
    validate2: str = validate_ingredients("dragon scales")
    print(f"validate_ingredients('fire air'): {validate1}")
    print(f"validate_ingredients('dragon scales'): {validate2}")

    print("\nTesting spell recording with validation:")
    record1: str = record_spell("Fireball", "fire air")
    record2: str = record_spell("Dark Magic", "shadow")
    print(f"record_spell('Fireball', 'fire air'): {record1}")
    print(f"record_spell('Dark Magic', 'shadow'): {record2}")

    print("\nTesting late import technique:")
    record: str = record_spell("Lightning", "air")
    print(f"record_spell('Lightning', 'air'): {record}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
