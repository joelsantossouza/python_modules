from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


class AggressiveStrategy(GameStrategy):
    """
    Strategy that prioritize attack and dealing damage,
    chosing low-cost creatures first for board presence
    """

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if not isinstance(hand, list):
            return None
        hand = list[Card] = [
            card for card in hand if isinstance(card, Card)
        ]
        sorted(hand, key=lambda card: card._info["cost"])
        best_targets: list[Card] = self.prioritize_targets(battlefield)
        return {
            "best_cards": hand,
            "best_targets": best_targets
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not isinstance(available_targets, list) or not available_targets:
            return None
        targets: list[Card] = [
            target for target in available_targets if isinstance(target, (CreatureCard, EliteCard))
        ]
        sorted(targets, key=lambda card: card._info["health"])
        return targets
