from inspect import getmembers, isfunction
from ex0.Card import Card
from ex0 import CreatureCard
from ex2 import Combatable, Magical, EliteCard


if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    card: list[str] = [n for n, _ in getmembers(Card, isfunction)]
    combatable: list[str] = [n for n, _ in getmembers(Combatable, isfunction)]
    magical: list[str] = [n for n, _ in getmembers(Magical, isfunction)]

    print(f" - Card: {card}")
    print(f" - Combatable: {combatable}")
    print(f" - Magical: {magical}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior: EliteCard = EliteCard(
        "Arcane Warrior", 10, "Legendary", 6, 3, 1, 10
    )
    goblin: CreatureCard = CreatureCard("Goblin", 3, "Legendary", 3, 5)
    print(f"Arcane Warrior: {arcane_warrior.get_card_info()}")
    print(f"Goblin: {goblin.get_card_info()}")

    print("\nCombat phase:")
    print(f"Attack result: {arcane_warrior.attack(goblin)}")
    print(f"Defense result: {arcane_warrior.defend(5)}")
    print(f"Update stats: {arcane_warrior.get_combat_stats()}")

    print("\nMagic phase:")
    targets: list[str] = ["Enemy1", "Enemy2"]
    print(f"Mana before: {arcane_warrior.get_magic_stats()}")
    print(f"Spell cast: {arcane_warrior.cast_spell("Fireball", targets)}")
    print(f"Mana after: {arcane_warrior.get_magic_stats()}")
    print(f"Mana channel: {arcane_warrior.channel_mana(1000)}")

    print("\nMultiple interface implementation successful!")
