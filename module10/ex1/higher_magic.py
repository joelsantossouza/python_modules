from typing import Callable


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combine two spells"""
    try:
        return lambda arg: (spell1(arg), spell2(arg))
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplify spell power"""
    try:
        return lambda: base_spell() * multiplier
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Cast spell conditionally"""
    try:
        return lambda arg: spell(arg) if condition(arg) else "Spell fizzled"
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


def spell_sequence(spells: list[callable]) -> callable:
    """Create Spell sequence"""
    try:
        return lambda arg: [spell(arg) for spell in spells]
    except Exception as e:
        print(f"ERROR: {e}")
        exit(1)


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combiner: Callable = spell_combiner(
        lambda target: f"Fireball hits {target}",
        lambda target: f"Heals {target}"
    )
    print(f"Combined spell result: {combiner('Dragon')}")

    print("\nTesting power amplifier...")
    fireball: Callable = lambda: 10
    amplifier: Callable = power_amplifier(
        fireball, 3
    )
    print(f"Original: {fireball()}, Amplified: {amplifier()}")

    print("\nTesting conditional caster...")
    conditional: Callable = conditional_caster(
        lambda spell: spell[:6] == "spell:",
        lambda spell: f"{spell} is valid -> doing spell"
    )
    good_input: str = "spell: fire"
    bad_input: str = "water"
    print(f"Input spell [{good_input}]: {conditional(good_input)}")
    print(f"Input spell [{bad_input}]: {conditional(bad_input)}")

    print("\nTesting spell sequence...")
    sequence: Callable = spell_sequence(
        [combiner, conditional, lambda string: f"{string} OK"]
    )
