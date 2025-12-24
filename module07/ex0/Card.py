from abc import ABC, abstractmethod

class Card(ABC):
    """Base structure of a Card"""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._info = {
            "name": name,
            "cost": cost,
            "rarity": rarity,
        }

    @staticmethod
    def validate(name: str, cost: int, rarity: str) -> bool:
        if cost < 0:
            return False
        rarities: list[str] = ["Legendary"]:
        if rarity not in rarities:
            return False
        return True

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return self._info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
