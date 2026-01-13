from typing import Any, Callable


def mage_counter() -> callable:
    """Create a counting closure"""
    calls: int = 0

    def func() -> int:
        """Return number of times it was called"""
        nonlocal calls
        calls += 1
        return calls
    return func


def spell_accumulator(initial_power: int) -> callable:
    """Create power accumulator"""
    if not isinstance(initial_power, int):
        return None
    power: int = initial_power

    def accumulator(amount: int) -> int:
        """Accumulate the total power"""
        if isinstance(amount, int):
            nonlocal power
            power += amount
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """Create enchantment functions"""
    if not isinstance(enchantment_type, str):
        return None
    enchantment: str = enchantment_type

    def enchant(item: str) -> str:
        """Return enchantment items"""
        if not isinstance(item, str):
            return None
        return f"{enchantment} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    """Create a memory management system"""
    memory: dict[Any] = {}

    def store(key: Any, value: Any) -> None:
        """Store new values into memory"""
        memory[key] = value

    def recall(key: Any) -> Any:
        """Returns stored values into memory"""
        try:
            return memory[key]
        except Exception:
            return "Memory not found"
    return {
        "store": store,
        "recall": recall,
    }


if __name__ == "__main__":
    print("\nTesting mage counter...")
    count_calls: Callable = mage_counter()
    for i in range(5):
        print(f"Call {i + 1}: {count_calls()}")

    print("\nTesting spell accumulator...")
    accumulator: Callable = spell_accumulator(5)
    for _ in range(3):
        print(f"Total power: {accumulator(5)}")

    print("\nTesting enchantment factory...")
    flaming: Callable = enchantment_factory("Flaming")
    frozen: Callable = enchantment_factory("Frozen")
    items: list[str] = ["Sword", "Shield", "Ring"]
    for item in items:
        print(f"{flaming(item)} -- {frozen(item)}")

    print("\nTesting memory vault...")
    mem: dict = memory_vault()
    print(f"Non existing key: {mem['recall']('name')}")
    mem['store']("name", "joel")
    print(f"Key('name') value added: {mem['recall']('name')}")
    mem['store']("name", 123456)
    print(f"Key('name') value updated: {mem['recall']('name')}")
