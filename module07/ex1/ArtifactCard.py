from ex0.Card import Card
from sys import stderr


class ArtifactCard(Card):
    """Card with hability to modify permanent game aspects"""

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        if not self.validate(name, cost, rarity, durability, effect):
            print(
                f"ArtifactCardError: Invalid input to create '{name}'",
                file=stderr
            )
            exit(1)
        super().__init__(name, cost, rarity)
        self.__active: bool = True
        self._info |= {
            "type": "Artifact",
            "durability": durability,
            "effect": effect,
            "attack": 0
        }

    def validate(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        if not isinstance(durability, int) or durability <= 0:
            return False
        if not isinstance(effect, str):
            return False
        return True

    def play(self, game_state: dict) -> dict:
        if not self.__active:
            return None
        return {
            "card_played": self._info["name"],
            "mana_used": self._info["cost"],
            "effect": self._info["effect"]
        }

    def destroy(self) -> None:
        self.__active = False

    def activate_ability(self) -> dict:
        self.__active = True
        return {
            "artifact": self._info["name"],
            "effect": self._info["effect"],
            "durability": self._info["durability"],
            "activated": True
        }
