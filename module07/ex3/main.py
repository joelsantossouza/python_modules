from ex3 import GameEngine, FantasyCardFactory, AggressiveStrategy

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    game: GameEngine = GameEngine()
    game.configure_engine(FantasyCardFactory(), AggressiveStrategy())
    print(f"Factory: {game.factory_used}")
    print(f"Strategy: {game.strategy_used}")
    print(f"Available types: {game.factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    cards_names: list[str] = [
        card._info["name"] for card in game.hand
    ]
    print(f"Hand: {cards_names}")

    print("\nTurn execution:")
    print(f"Strategy: {game.strategy_used}")
    print(f"Actions: {game.simulate_turn()}")

    print("\nGame Report:")
    print(game.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )
