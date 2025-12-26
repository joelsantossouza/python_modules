from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """Abstract Base Class providing an interface to strategies in game"""

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...

    @abstractmethod
    def get_strategy_name(self) -> str:
        ...

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        ...
