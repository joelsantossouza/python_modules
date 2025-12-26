from ex0.Card import Card
from sys import stderr


class SpellCard(Card):
    """Cards specialized in instant magic effects"""

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        if not self.validate(name, cost, rarity, effect_type):
            print(
                f"SpellCardError: Invalid input to create '{name}'",
                file=stderr
            )
            exit(1)
        attack: int = 0
        if effect_type == "damage":
            effect_type = "Deal 3 damage to target"
            attack = 3
        elif effect_type == "heal":
            effect_type = "Restore 3 health points"
        elif effect_type == "buff":
            effect_type = "Grant +2 attack points"
        elif effect_type == "unbuff":
            effect_type = "Reduce target attack by 2"
        super().__init__(name, cost, rarity)
        self._info |= {
            "type": "Spell",
            "effect": effect_type,
            "attack": attack
        }

    def validate(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        effects_type: list[str] = [
            "damage", "heal", "buff", "unbuff"
        ]
        if effect_type not in effects_type:
            return False
        return True

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._info["name"],
            "mana_used": self._info["cost"],
            "effect": self._info["effect"]
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self._info["name"],
            "effect": self._info["effect"],
            "targets": targets,
            "resolved": True
        }
