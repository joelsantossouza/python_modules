from ex4 import TournamentPlatform, TournamentCard


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    tournament: TournamentPlatform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    cards: list[dict] = [
        {"name": "Fire Dragon", "id": "dragon_001"},
        {"name": "Ice Wizard", "id": "wizard_001"}
    ]
    for card in cards:
        created_card: TournamentCard = TournamentCard(
            card["name"], 3, "Legendary", 3, 5, 1, 6, card["id"]
        )
        tournament.register_card(created_card)
        print(f"\n{card['name']} (ID: {card['id']}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        info: dict = created_card.get_rank_info()
        print(f" - Rating: {info['rating']}")
        print(f" - Record: {info['wins']}-{info['losses']}")

    print("\nCreating tournament match...")
    match: dict = tournament.create_match(cards[0]["id"], cards[1]["id"])
    print(f"Match result: {match}")

    print("\nTournament Leaderboard:")
    leaderboard: list[TournamentCard] = tournament.get_leaderboard()
    for i, card in enumerate(leaderboard):
        info: dict = card.get_rank_info()
        print(
            f"{i + 1}- "
            f"{card._info['name']} - "
            f"Rating: {info['rating']} "
            f"({info['wins']}-{info['losses']})"
        )

    print("\nPlatform Report:")
    print(tournament.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
