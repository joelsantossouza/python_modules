import random
from ex0.Card import Card


class Deck:
    """Holds every Cards types polymorphically"""

    __cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.__cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.__cards):
            if card._info["name"] == card_name:
                del self.__cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        if self.__cards:
            return self.__cards.pop(0)
        else:
            return None

    def get_deck_stats(self) -> dict:
        stats: dict = {
            "total_cards": 0,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0
        }
        for card in self.__cards:
            card: dict = card.get_card_info()
            stats["total_cards"] += 1
            stats["avg_cost"] += card["cost"]
            if card["type"] == "Creature":
                stats["creatures"] += 1
            elif card["type"] == "Spell":
                stats["spells"] += 1
            elif card["type"] == "Artifact":
                stats["artifacts"] += 1
        if stats["total_cards"] > 0:
            stats["avg_cost"] /= stats["total_cards"]
        return stats
