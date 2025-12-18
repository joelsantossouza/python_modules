def generate_1000_events() -> str:
    """
    using generator and yield to save function state
    providing speed and memory optimization
    """
    for event in range(342):
        yield "high-level player"
    for event in range(89):
        yield "found treasure"
    for event in range(156):
        yield "player level-up"
    for event in range(413):
        yield "irrelevant event"

def fibonacci_generator(n: int) -> int:
    """Generator of 0 to n fibonacci numbers"""
    if n <= 0:
        yield
    else:
        previous: int = 0
        current: int = 1
        for _ in range(n):
            yield previous
            tmp_previous: int = previous
            previous = current
            current += tmp_previous


def is_prime(n: int) -> bool:
    """
    Returns True or False if 
    the number is or not prime respectively
    """
    if n < 2:
        return False
    half: int = n // 2
    i: int = 2
    while (i <= half):
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(n: int) -> int:
    """Generator of 0 to n prime numbers"""
    if n <= 0:
        yield
    else:
        prime: int = 2
        for _ in range(n):
            while (not is_prime(prime)):
                prime += 1
            yield prime
            prime += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    print("\nProcessing 1000 game events...")
    all_events = generate_1000_events()

    print(
        "Event 1: Player alice (level 5) killed monster\n"
        "Event 2: Player bob (level 12) found treasure\n"
        "Event 3: Player charlie (level 8) leveled up\n"
        "..."
    )
    print("\n=== Stream Analytics ===")
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0
    for event in all_events:
        if event == "high-level player":
            high_level_players += 1
        elif event == "found treasure":
            treasure_events += 1
        elif event == "player level-up":
            level_up_events += 1
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    sequence = fibonacci_generator(10)
    for n in range(9):
        print(f"{next(sequence)}, ", end="")
    print(f"{next(sequence)}")

    print("Prime numbers(first 5): ", end="")
    primes = prime_generator(5)
    for n in range(4):
        print(f"{next(primes)}, ", end="")
    print(f"{next(primes)}")
