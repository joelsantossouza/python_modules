from ex0 import CreatureCard

if __name__ == "__main__":
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")
    mana: int = 6
    fire_dragon: CreatureCard = CreatureCard(
        "Fire Dragon", 5, "Legendary", 7, 5
    )
    goblin_warrior: CreatureCard = CreatureCard(
        "Goblin Warrior", 3, "Legendary", 7, 1
    )

    print("\nCreatureCard Info:")
    print(f"Fire Dragon: {fire_dragon.get_card_info()}")
    print(f"Goblin Warrior: {goblin_warrior.get_card_info()}")

    print(f"\nPlaying Fire Dragon with {mana} mana available:")
    print(f"Playable: {fire_dragon.is_playable(mana)}")
    result: dict = fire_dragon.play(None)
    mana -= result["mana_used"]
    print(f"Play result: {result}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print("\nUpdate values info")
    print(f"Fire Dragon: {fire_dragon.get_card_info()}")
    print(f"Goblin Warrior: {goblin_warrior.get_card_info()}")

    print(f"\nTesting insufficient mana ({mana} available):")
    print(f"Playable: {fire_dragon.is_playable(mana)}")

    print("\nAbstract pattern successfully demonstrated!")
