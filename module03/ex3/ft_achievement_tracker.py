if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    print(f"Player alice achievements: {alice}")
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    print(f"Player bob achievements: {bob}")
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon"}
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique = alice | bob | charlie
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    common = alice & bob & charlie
    print(f"\nCommon to all players: {common}")
