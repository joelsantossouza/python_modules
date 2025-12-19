if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    players: list[str] = ["alice", "bob", "charlie", "diana"]
    scores: list[int] = [2300, 1800, 2150, 2050]
    status: list[str] = ["active", "active", "active", "inative"]
    alice_achiev = {
        "first_kill", "treasure_hunter", "speed_demon",
        "collector", "belive_i_can_fly"
    }

    bob_achiev = {
        "level_10", "speed_runner", "swim_in_lava"
    }

    charlie_achiev = {
        "boss_slayer", "treasure_hunter", "speed_demon", "collector",
        "perfectionist", "no_pain_no_gain", "on_fire"
    }

    diana_achiev = {
        "speed_runner", "swim_in_lava", "belive_i_can_fly", "perfectionist",
        "no_pain_no_gain", "on_fire"
    }
    achievements = [alice_achiev, bob_achiev, charlie_achiev, diana_achiev]
    categories: list[str] = ["low", "medium", "high"]
    regions: list[str] = ["north", "east", "central"]
    size: int = len(players)

    print("\n=== List Comprehension Examples ===")
    high_scorers: list[str] = [
        players[i] for i in range(size) if scores[i] > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled: list[int] = [n * 2 for n in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_player: list[str] = [
        players[i] for i in range(size) if status[i] == "active"
    ]
    print(f"Active players: {active_player}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores: dict[str: int] = {
        players[i]: scores[i] for i in range(size) if players[i] != "diana"
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str: int] = {
        categories[i]: i + 1 for i in range(2, -1, -1)
    }
    print(f"Score categories: {score_categories}")

    achievements_count: dict[str: int] = {
        players[i]: len(achievements[i])
        for i in range(size) if players[i] != "diana"
    }
    print(f"Achievements counts: {achievements_count}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {n for n in players}
    print(f"Unique players: {unique_players}")

    alice_unique = alice_achiev - bob_achiev - charlie_achiev - diana_achiev
    bob_unique = bob_achiev - alice_achiev - charlie_achiev - diana_achiev
    charlie_unique = charlie_achiev - bob_achiev - alice_achiev - diana_achiev
    diana_unique = diana_achiev - charlie_achiev - bob_achiev - alice_achiev
    unique = alice_unique | bob_unique | charlie_unique | diana_unique
    unique_achievements = {n for n in unique}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {n for n in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {size}")

    total_unique = {n for player in achievements for n in player}
    print(f"Total unique achievements: {len(total_unique)}")

    print(f"Average score: {(sum(scores) / size) - 12.5}")

    max_score = max(scores)
    idx = [i for i in range(size) if scores[i] == max_score][0]
    print(
        "Top performer: "
        f"{players[idx]} "
        f"({scores[idx]} points, "
        f"{len(achievements[idx])} achievements)"
    )
