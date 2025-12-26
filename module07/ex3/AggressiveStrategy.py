from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    """
    Strategy that prioritize attack and dealing damage,
    chosing low-cost creatures first for board presence
    """

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return

    def prioritize_targets(self, available_targets: list) -> list:
        if not isinstance(available_target, list) not available_target:
            return None
        one_hit_kill: list[CreatureCard] = []
        more_hits_kill: list[CreatureCard] = []
        for target in available_targets:
