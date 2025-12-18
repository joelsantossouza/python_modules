if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice: set[str] = {
        "first_kill", "level_10", "treasure_hunter", "speed_demon"
    }
    print(f"Player alice achievements: {alice}")
    bob: set[str] = {"first_kill", "level_10", "boss_slayer", "collector"}
    print(f"Player bob achievements: {bob}")
    charlie: set[str] = {
        "level_10", "treasure_hunter", "boss_slayer",
        "speed_demon", "perfectionist"
    }
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    unique: set[str] = alice | bob | charlie
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}")

    common: set[str] = alice & bob & charlie
    print(f"\nCommon to all players: {common}")

    alice_unique: set[str] = alice - bob - charlie
    bob_unique: set[str] = bob - charlie - alice
    charlie_unique: set[str] = charlie - alice - bob

    rare: set[str] = alice_unique | bob_unique | charlie_unique
    print(f"Rare achievements (1 player): {rare}")

    alice_vs_bob_common: set[str] = alice & bob
    print(f"\nAlice vs Bob common: {alice_vs_bob_common}")

    alice_unique_bob: set[str] = alice - bob
    print(f"Alice unique: {alice_unique_bob}")

    bob_unique_alice: set[str] = bob - alice
    print(f"Bob unique: {bob_unique_alice}")
