from ex1 import Deck, SpellCard, ArtifactCard
from ex0.Card import Card
from ex0 import CreatureCard


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck: Deck = Deck()
    cards: list[Card] = [
        SpellCard("Lightning Bolt", 3, "Legendary", "damage"),
        SpellCard("Cure Magic", 5, "Legendary", "heal"),
        CreatureCard("Fire Dragon", 5, "Legendary", 1, 6),
        ArtifactCard("Mana Crystal", 4, "Legendary", 5, "+1 mana per turn"),
    ]
    for card in cards:
        deck.add_card(card)
    print(f"Deck stats {deck.get_deck_stats()}")

    deck.remove_card("Cure Magic")
    print("\nDrawing and playing cards:")
    deck.shuffle()
    card = deck.draw_card()
    while (card):
        info: dict = card.get_card_info()
        print(f"\nDrew: {info["name"]} ({info["type"]})")
        print(f"Play result: {card.play(None)}")
        card = deck.draw_card()

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )
