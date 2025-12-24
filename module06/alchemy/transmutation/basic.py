from alchemy.elements import create_fire, create_earth

def lead_to_gold() -> str:
    """Convert lead to gold"""
    fire: str = create_fire()
    return f"Lead transmuted to gold using {fire}"

def stone_to_gem() -> str:
    """Convert stone to gem"""
    earth: str = create_earth()
    return f"Stone transmuted to gem using {earth}"
