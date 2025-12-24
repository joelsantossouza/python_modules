from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """Create a philosophers stone"""
    gold: str = lead_to_gold()
    healing: str = healing_potion()
    return f"Philosopher’s stone created using {gold} " \
        f"and {healing}"


def elixir_of_life() -> str:
    """Create a elixir of life"""
    return "Elixir of life: eternal youth achieved!"
