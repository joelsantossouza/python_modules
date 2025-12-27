from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """Game orchestrator"""

    def __init__(self) -> None:
        self.factory: CardFactory = None
        self.strategy: GameStrategy = None
        self.turns_simulated: int = 0
        self.strategy_used: str = None
        self.factory_used: str = None
        self.total_damage: int = 0
        self.cards_created: int = 0
        self.hand: list[Card] = []
        self.battlefield: list[Card] = []
        self.mana: int = 6

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        if isinstance(factory, CardFactory):
            self.factory = factory
            self.factory_used = factory.get_factory_name()
            self.hand = factory.create_themed_deck(7)["deck"]
            self.battlefield = factory.create_themed_deck(4)["deck"]
            self.cards_created = 7
        if isinstance(strategy, GameStrategy):
            self.strategy = strategy
            self.strategy_used = strategy.get_strategy_name()

    def simulate_turn(self) -> dict:
        self.turns_simulated += 1
        actions: dict = self.strategy.execute_turn(self.hand, self.battlefield)
        cards_played: list[Card] = []
        targets_attacked: list[Card] = []
        mana_used: int = 0
        damage_dealt: int = 0
        for card in actions["best_cards"]:
            if card._info["cost"] > self.mana or not actions["best_targets"]:
                break
            cards_played.append(card._info["name"])
            targets_attacked.append(actions["best_targets"][0]._info["name"])
            mana_used += card._info["cost"]
            self.mana -= card._info["cost"]
            damage_dealt += card._info["attack"]
            actions["best_targets"][0]._info["health"] -= card._info["attack"]
            if actions["best_targets"][0]._info["health"] <= 0:
                actions["best_targets"][0]._info["health"] = 0
                self.battlefield.remove(actions["best_targets"][0])
                del actions["best_targets"][0]
        self.total_damage += damage_dealt
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy_used,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
