class CreatureCard(Card):
    """Structure of creature's type Card"""

    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        if not self.validate(name, cost, rarity, attack, health):
            print("ERROR: Invalid input to create a CreatureCard")
            return
        super().__init__(name, cost, rarity)
        super()._info += {
            "type": "Creature",
            "attack": attack,
            "health": health
        }

    @staticmethod
    def validate(name: str, cost: int, rarity: str, attack: int, health: int) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        if attack < 0 || health < 0:
            return False
        return True

    def play(self, game_state: dict) -> dict:

    def attack_target(self, target) -> dict:
