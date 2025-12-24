from ex0.Card import Card
from sys import stderr

class CreatureCard(Card):
    """Structure of creature's type Card"""

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        if not self.validate(name, cost, rarity, attack, health):
            try:
                raise Exception(f"CreatureCardError: Invalid input to create '{name}'")
            except Exception as e:
                print(e, file=stderr)
                exit(1)
        super().__init__(name, cost, rarity)
        self._info |= {
            "type": "Creature",
            "attack": attack,
            "health": health
        }

    def validate(self, name: str, cost: int, rarity: str, attack: int, health: int) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        if attack <= 0 or health <= 0:
            return False
        return True

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._info["name"],
            "mana_used": self._info["cost"],
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        if not isinstance(target, Card):
            return None
        decreased_health: int = target._info["health"] - self._info["attack"]
        if decreased_health < 0:
            decreased_health = 0
        target._info["health"] = decreased_health
        return {
            "attacker": self._info["name"],
            "target": target._info["name"],
            "damage_dealt": self._info["attack"],
            "combat_resolved": True
        }
