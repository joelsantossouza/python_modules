if __name__ == "__main__":
    print("=== Player Inventory System ===")
    sword: dict[] = {
        "type": "(weapon, rare)",
        "quantity": 1,
        "price": 500
    }

    potion: dict[] = {
        "type": "(consumable, common)",
        "quantity": 5,
        "price": 50
    }

    shield: dict[] = {
        "type": "(armor, uncommon)",
        "quantity": 1,
        "price": 200
    }

    alice: dict[] = {
        "weapon": sword,
        "consumable": potion,
        "armor": shield,
        "gold": 950,
    }
    print("\n=== Alice's Inventory ===")
