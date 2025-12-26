def validate_ingredients(ingredients: str) -> str:
    if not isinstance(ingredients, str):
        return f"{ingredients} - INVALID"
    elements: list[str] = ["fire", "water", "earth", "air"]
    each_ingredient = ingredients.split()
    for ingredient in each_ingredient:
        if ingredient not in elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
