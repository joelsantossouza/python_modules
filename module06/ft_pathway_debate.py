from alchemy.transmutation import lead_to_gold, stone_to_gem, \
    philosophers_stone, elixir_of_life
import alchemy

if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    print("\nTesting Absolute Imports (from basic.py):")
    gold: str = lead_to_gold()
    gem: str = stone_to_gem()
    print(f"lead_to_gold(): {gold}")
    print(f"stone_to_gem(): {gem}")

    print("\nTesting Relative Imports (from advanced.py):")
    philo_stone: str = philosophers_stone()
    print(f"philosophers_stone(): {philo_stone}")
    elixir: str = elixir_of_life()
    print(f"elixir_of_life(): {elixir}")

    print("\nTesting Package Access:")
    gold: str = alchemy.transmutation.lead_to_gold()
    philo_stone: str = alchemy.transmutation.philosophers_stone()
    print(f"alchemy.transmutation.lead_to_gold(): {gold}")
    print(f"alchemy.transmutation.philosophers_stone(): {philo_stone}")

    print("\nBoth pathways work! Absolute: clear, Relative: concise")
