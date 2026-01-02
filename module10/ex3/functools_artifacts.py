from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers"""
    try:
        if operation == "add":
            return reduce(add, spells)
        if operation == "multiply":
            return reduce(mul, spells)
        if operation == "max":
            return reduce(max, spells)
        if operation == "min":
            return reduce(min, spells)
        return None
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """Create partial applications"""
    try:
        fire_enchant: Callable = partial(
            base_enchantment, 50, "fire_enchant"
        )
        ice_enchant: Callable = partial(
            base_enchantment, 50, "ice_enchant"
        )
        lightning_enchant: Callable = partial(
            base_enchantment, 50, "lightning_enchant"
        )
        return {
            "fire_enchant": fire_enchant,
            "ice_enchant": ice_enchant,
            "lightning_enchant": lightning_enchant,
        }
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    """Cached fibonacci"""
    if not isinstance(n, int) or n < 0:
        return None
    previous: int = 0
    current: int = 1
    for _ in range(n):
        tmp_previous: int = previous
        previous = current
        current += tmp_previous
    return previous


def spell_dispatcher() -> callable:
    """Create single dispatch system"""
    @singledispatch
    def dispatch(input: Any) -> str:
        """Geral behaviour of unknown spells type"""
        return f"Unknown spell '{input}' type"

    @dispatch.register(int)
    def dispatch_int(input: int) -> str:
        """Damage spells behaviour"""
        return f"Damage spell dealing {input} damage"

    @dispatch.register(str)
    def dispatch_str(input: str) -> str:
        """Enchantment spells behaviour"""
        return f"Enchantment applied: {input}"

    @dispatch.register(list)
    def dispatch_list(inputs: list) -> list[str]:
        """Multi-cast spells behaviour"""
        return [dispatch(input) for input in inputs]
    return dispatch


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells: list[int] = [20, 12, 0, 99, 42]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print(f"Unknown: {spell_reducer(spells, 'unknown')}")

    print("\nTesting partial enchanter...")
    enchanter: Callable = lambda power, element, target: \
        f"{power} {element} {target}"
    applications: dict = partial_enchanter(enchanter)
    print(applications['fire_enchant']("Sword"))
    print(applications['ice_enchant']("Bow"))
    print(applications['lightning_enchant']("Shild"))

    print("\nTesting memoized fibonacci...")
    print(f"Fist time: {memoized_fibonacci(5)}")
    print(f"Second time: {memoized_fibonacci(5)}")

    print("\nTesting spell dispatcher...")
    cast_spell: Callable = spell_dispatcher()
    print(f"Integer: {cast_spell(10)}")
    print(f"String: {cast_spell('Sharpness')}")
    print(f"List: {cast_spell([100, "Flame", 99.9])}")
