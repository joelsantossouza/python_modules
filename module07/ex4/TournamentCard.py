from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from sys import stderr


class TournamentCard(Card, Combatable, Rankable):
    """Card specialized in Combat and Ranking system"""

    __max_mana: int = 100

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, defense: int, mana: int, id: str) -> None:
        if not self.validate(name, cost, rarity, attack,
                             health, defense, mana, id):
            print(
                f"TournamentCardError: Invalid input to create '{name}'",
                file=stderr
            )
            exit(1)
        super().__init__(name, cost, rarity)
        self.__rating: int = 1200
        self.__wins: int = 0
        self.__losses: int = 0
        self._info |= {
            "type": "Tournament Card",
            "attack": attack,
            "health": health,
            "defense": defense,
            "mana": mana,
            "id": id
        }

    def validate(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, defense: int, mana: int, id: str) -> bool:
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
        if not isinstance(id, str):
            return False
        return True

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self._info["name"],
            "mana_used": self._info["cost"],
            "effect": None
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

    def calculate_rating(self) -> int:
        return self.__rating

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins <= 0:
            return
        self.__wins += wins
        self.__rating += wins * 20

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses <= 0:
            return
        self.__losses += losses
        self.__rating -= losses * 20

    def get_rank_info(self) -> dict:
        return {
            "rating": self.__rating,
            "wins": self.__wins,
            "losses": self.__losses
        }
