import alchemy

if __name__ == "__main__":
    print("\n=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    try:
        fire: str = alchemy.elements.create_fire()
    except Exception as e:
        fire: str = e
    print(f"alchemy.elements.create_fire(): {fire}")

    try:
        water: str = alchemy.elements.create_water()
    except Exception as e:
        water: str = e
    print(f"alchemy.elements.create_water(): {water}")

    try:
        earth: str = alchemy.elements.create_earth()
    except Exception as e:
        earth: str = e
    print(f"alchemy.elements.create_earth(): {earth}")

    try:
        air: str = alchemy.elements.create_air()
    except Exception as e:
        air: str = e
    print(f"alchemy.elements.create_air(): {air}")


    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        fire: str = alchemy.create_fire()
    except Exception as e:
        fire: str = e
    print(f"alchemy.create_fire(): {fire}")

    try:
        water: str = alchemy.create_water()
    except Exception as e:
        water: str = e
    print(f"alchemy.create_water(): {water}")

    try:
        earth: str = alchemy.create_earth()
    except Exception:
        earth: str = "AttributeError - not exposed"
    print(f"alchemy.create_earth(): {earth}")

    try:
        air: str = alchemy.create_air()
    except Exception:
        air: str = "AttributeError - not exposed"
    print(f"alchemy.create_air(): {air}")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")
