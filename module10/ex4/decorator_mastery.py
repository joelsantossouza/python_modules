from time import time
from functools import wraps
from random import randint


def spell_timer(func: callable) -> callable:
    """Time execution decorator"""
    @wraps(func)
    def timer(*args, **kwargs) -> any:
        """Counts the execution time of a function"""
        print(f"Casting {func.__name__}")
        start: float = time()
        result: any = func(*args, **kwargs)
        print(f"Spell completed in {(time() - start):.6f} seconds")
        return result
    return timer


def power_validator(min_power: int) -> callable:
    """Parameterized validation decorator"""
    def decorator(func: callable) -> callable:
        """Decorator that validate power parameter"""
        @wraps(func)
        def validator(*args, **kwargs) -> any:
            """Execute function if args[0] >= min_power"""
            if isinstance(args[0], int):
                if args[0] >= min_power:
                    return func(*args, **kwargs)
            else:
                try:
                    if kwargs['power'] >= min_power:
                        return func(*args, **kwargs)
                except Exception:
                    pass
            return "Insufficient power for this spell"
        return validator
    return decorator


def retry_spell(max_attempts: int) -> callable:
    """Retry decorator creator"""
    def decorator(func: callable) -> callable:
        """Retry decorator"""
        def new_func(*args, **kwargs) -> str:
            """Retry the func in max_attempts"""
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... ({i + 1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return new_func
    return decorator


class MageGuild:
    """Demonstrate staticmethod"""

    def __init__(self) -> None:
        return

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False
        for chr in name:
            if not chr.isalpha() and not chr.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Fireball caster"""
    for _ in range(1000000):
        pass
    return "Fireball cast!"


def kamehameha(power: int) -> str:
    """Energy attack"""
    return f"Spent {power} of power doing kamehameha!"


@retry_spell(3)
def try_spell() -> str:
    """Spell that randomly can success or fail"""
    if randint(0, 1) == 1:
        raise Exception("Spell Failed")
    return "Spell successfully casted"


if __name__ == "__main__":
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    validator: callable = power_validator(10)
    func_validated: callable = validator(kamehameha)
    print(f"Without validation: {kamehameha(5)}")
    print(f"With validation: {func_validated(5)}")

    print("\nTesting retry spell...")
    print(try_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("jo"))
    print(MageGuild.validate_mage_name("joel42"))
    print(MageGuild.validate_mage_name("joel!"))
    print(MageGuild.validate_mage_name("joel_Souza"))
    print(MageGuild.validate_mage_name("joel"))
    print(MageGuild.validate_mage_name("joel Souza"))
    mage_guild: MageGuild = MageGuild()
    print(mage_guild.cast_spell("Fireball", power=9))
    print(mage_guild.cast_spell("Fireball", power=11))
