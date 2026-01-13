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
        def validator(*args, **kwargs) -> any:
            """Execute function if args[0] >= min_power"""
            if args[0] >= min_power:
                return func(*args, **kwargs)
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
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return

    def cast_spell(self, spell_name: str, power: int) -> str:
        return


@spell_timer
def fireball() -> str:
    """Fireball caster"""
    for _ in range(1000000):
        pass
    return "Fireball cast!"


def kamehameha(power: int) -> str:
    """Energy attack"""
    return f"Spent {power} of power doing kamehameha!"


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
    decorator_retry: callable = retry_spell(3)
    retry_try_spell: callable = decorator_retry(try_spell)
    print(retry_try_spell())

    print("\nTesting MageGuild...")
