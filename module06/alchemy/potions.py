from .elements import create_fire, create_water, create_earth, create_air

def healing_potion() -> str:
    """Create a healing potion"""
    fire: str = create_fire()
    water: str = create_water()
    return f"Healing potion brewed with {fire} and {water}"

def strength_potion() -> str:
    """Create a strength potion"""
    earth: str = create_earth()
    fire: str = create_fire()
    return f"Strength potion brewed with {earth} and {fire}"

def invisibility_potion() -> str:
    """Create a invisibility potion"""
    air: str = create_air()
    water: str = create_water()
    return f"Invisibility potion brewed with {air} and {water}"

def wisdom_potion() -> str:
    """Create a wisdom potion"""
    fire: str = create_fire()
    water: str = create_water()
    earth: str = create_earth()
    air: str = create_air()
    return f"Wisdom potion brewed with all elements:\n" \
        f" - {fire}\n" \
        f" - {water}\n" \
        f" - {earth}\n" \
        f" - {air}\n"
