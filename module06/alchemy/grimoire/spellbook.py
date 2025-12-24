def record_spell(spell_name: str, ingredients: str) -> str:
    from . import validate_ingredients
    validation: str = validate_ingredients(ingredients)
    if validation[8:] == " - VALID":
        return f"Spell recorded: {spell_name} ({validation})"
    return f"Spell rejected: {spell_name} ({validation})"
