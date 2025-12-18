if __name__ == "__main__":
    print("=== Player Inventory System ===")
    sword: dict[None] = {
        "name": "sword",
        "type": "(weapon, rare)",
        "quantity": 1,
        "price": 500
    }

    potion1: dict[None] = {
        "name": "potion",
        "type": "(consumable, common)",
        "quantity": 5,
        "price": 50
    }

    potion2: dict[None] = {
        "name": "potion",
        "type": "(consumable, common)",
        "quantity": 0,
        "price": 50
    }

    shield: dict[None] = {
        "name": "shield",
        "type": "(armor, uncommon)",
        "quantity": 1,
        "price": 200
    }

    magic_ring: dict[None] = {
        "name": "magic_ring",
        "type": "(armor, rare)",
        "quantity": 1,
        "price": 300
    }

    alice: dict[None] = {
        "weapons": sword,
        "consumables": potion1,
        "armors": shield,
        "value": 950,
        "items": 7
    }

    bob: dict[None] = {
        "weapons": None,
        "consumables": potion2,
        "armors": magic_ring,
        "value": 300,
        "items": 1
    }

    print("\n=== Alice's Inventory ===")
    weapon: dict[None] = alice["weapons"]
    print(
        f"{weapon["name"]} "
        f"{weapon["type"]}: "
        f"{weapon["quantity"]}x @ "
        f"{weapon["price"]} gold each = "
        f"{weapon["price"] * weapon["quantity"]} gold"
    )

    consumable: dict[None] = alice["consumables"]
    print(
        f"{consumable["name"]} "
        f"{consumable["type"]}: "
        f"{consumable["quantity"]}x @ "
        f"{consumable["price"]} gold each = "
        f"{consumable["price"] * consumable["quantity"]} gold"
    )

    armor: dict[None] = alice["armors"]
    print(
        f"{armor["name"]} "
        f"{armor["type"]}: "
        f"{armor["quantity"]}x @ "
        f"{armor["price"]} gold each = "
        f"{armor["price"] * armor["quantity"]} gold"
    )

    print(f"\nInventory value: {alice["value"]} gold")
    print(f"Item count: {alice["items"]} items")
    print(
        "Categories: "
        f"weapon({weapon["quantity"]}), "
        f"consumable({consumable["quantity"]}), "
        f"armor({armor["quantity"]})"
    )

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    alice["consumables"]["quantity"] -= 2
    alice["items"] -= 2
    alice["value"] -= 2 * consumable["price"]
    bob["consumables"]["quantity"] += 2
    bob["items"] += 2
    bob["value"] += 2 * consumable["price"]
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice["consumables"]["quantity"]}")
    print(f"Bob potions: {bob["consumables"]["quantity"]}")

    print("\n=== Inventory Analytics ===")
    alice_value = alice["value"]
    bob_value = bob["value"]
    print("Most valuable player: ", end="")
    if alice_value > bob_value:
        print(f"Alice ({alice_value} gold)")
    else:
        print(f"Bob ({bob_value} gold)")

    alice_items = alice["items"]
    bob_items = bob["items"]
    print("Most items: ", end="")
    if alice_items > bob_items:
        print(f"Alice ({alice_items} items)")
    else:
        print(f"Bob ({bob_items} items)")

    print(
        "Rarest items: "
        f"{sword["name"]}, "
        f"{magic_ring["name"]}"
    )
