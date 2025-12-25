class SpellCard(Card):
    """Cards specialized in instant magic effects"""

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        if not self.validate(name, cost, rarity, effect_type):
            print(
                f"SpellCardError: Invalid input to create '{name}'",
                file=stderr
            )
            exit(1)

    def validate(self, name: str, cost: int, rarity: str, effect_type: str) -> bool:
        if not super().validate(name, cost, rarity):
            return False
        effects_type = list[str] = [
            "damage", "heal", "buff", "debuff"
        ]
        if effect_type not in effects_type:
            return False
        return True


    def play(self, game_state: dict) -> dict:
        return

    def resolve_effect(self, targets: list) -> dict:
        return
