from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from sys import stderr


class EliteCard(Card, Combatable, Magical):
    """Card that has properties of a Card & combatable and magical cards"""

    __max_mana: int = 100

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int, mana: int) -> None:
        if not self.validate(name, cost, rarity,
                             attack, health, defense, mana):
            print(
                f"EliteCardError: Invalid input to create '{name}'",
                file=stderr
            )
            exit(1)
        super().__init__(name, cost, rarity)
        self._info |= {
            "type": "Elite Card",
            "attack": attack,
            "health": health,
            "defense": defense,
            "mana": mana
        }

    def validate(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, defense: int, mana: int) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        if not isinstance(attack, int) or not isinstance(health, int):
            return False
        if not isinstance(defense, int) or not isinstance(mana, int):
            return False
        if attack <= 0 or health <= 0:
            return False
        if defense < 0 or mana < 0 or mana > self.__max_mana:
            return False
        return True

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._info["name"],
            "mana_used": self._info["cost"],
            "effect": "Elite summoned to battlefield"
        }

    def attack(self, target) -> dict:
        if not isinstance(target, Card):
            return None
        return {
            "attacker": self._info["name"],
            "target": target._info["name"],
            "damage": self._info["attack"],
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int) or incoming_damage < 0:
            return None
        stats: dict = {
            "defender": self._info["name"],
            "damage_taken": 0,
            "damage_blocked": 0,
            "still_alive": True
        }
        if incoming_damage < self._info["defense"]:
            stats["damage_blocked"] = incoming_damage
        else:
            stats["damage_blocked"] = self._info["defense"]
        incoming_damage -= self._info["defense"]
        if incoming_damage < 0:
            incoming_damage = 0
        stats["damage_taken"] = incoming_damage
        self._info["health"] -= incoming_damage
        if self._info["health"] <= 0:
            self._info["health"] = 0
            stats["still_alive"] = False
        return stats

    def get_combat_stats(self) -> dict:
        return {
            "attack": self._info["attack"],
            "health": self._info["health"],
            "defense": self._info["defense"],
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if not isinstance(spell_name, str) or not isinstance(targets, list) \
                or self._info["mana"] < 4:
            return None
        self._info["mana"] -= 4
        return {
            "caster": self._info["name"],
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        if not isinstance(amount, int) or amount <= 0:
            return None
        self._info["mana"] += amount
        if self._info["mana"] > self.__max_mana:
            self._info["mana"] = self.__max_mana
        return {
            "channeled": amount,
            "total_mana": self._info["mana"]
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self._info["mana"],
            "max_mana": self.__max_mana
        }
