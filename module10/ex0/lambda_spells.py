def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts"""
    try:
        return sorted(artifacts, key=lambda artifact: artifact['power'])
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Filter mages by power"""
    try:
        if not isinstance(min_power, int):
            raise ValueError("Min_power must be integer")
        return list(filter(lambda mage: mage['power'] >= min_power, mages))
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names"""
    try:
        return list(map(lambda spell: f"* {spell} *", spells))
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def mage_stats(mages: list[dict]) -> dict:
    """Calculate statistics"""
    try:
        avg_power: float = 0
        if mages:
            avg_power = sum(mage['power'] for mage in mages) / len(mages)
        return {
            "max_power": max(mages, key=lambda mage: mage['power'])['power'],
            "min_power": min(mages, key=lambda mage: mage['power'])['power'],
            "avg_power": round(avg_power, 2)
        }
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifact: list[dict] = [
        {"name": "Staff", "power": 92, "type": "Mage"},
        {"name": "Orb", "power": 85, "type": "Crystal"},
        {"name": "Ring", "power": 20, "type": "Armor"},
    ]
    result: list[dict] = artifact_sorter(artifact)
    for i in range(len(artifact)):
        print(
            f"{i + 1}. {artifact[i]['name']} ({artifact[i]['power']} power)",
            end=" - "
        )
        print(
            f"{result[i]['name']} ({result[i]['power']} power)",
        )

    print("\nTesting power filter...")
    mages: list[dict] = [
        {"name": "Staff", "power": 92, "element": "Fire"},
        {"name": "Orb", "power": 85, "element": "Water"},
        {"name": "Ring", "power": 20, "element": "Air"},
    ]
    result: list[dict] = power_filter(mages, 80)
    print(f"Before: {mages}")
    print(f"After: {result}")

    print("\nTesting spell transformer...")
    spells: list[str] = [
        "Fireball", "Heal", "Shield"
    ]
    result: list[str] = spell_transformer(spells)
    print(f"Before: {spells}")
    print(f"After: {result}")

    print("\nTesting mage stats...")
    mages: list[dict] = [
        {"name": "Staff", "power": 92, "element": "Fire"},
        {"name": "Orb", "power": 85, "element": "Water"},
        {"name": "Ring", "power": 20, "element": "Air"},
    ]
    result: dict = mage_stats(mages)
    print(f"Before: {mages}")
    print(f"After: {result}")
