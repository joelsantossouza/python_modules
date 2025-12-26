def validate_ingredients(ingredients: str) -> str:
    if not isinstance(ingredients, str):
        return f"{ingredients} - INVALID"
    elements: list[str] = ["fire", "water", "earth", "air"]
    ingredients = ingredients.split()
    for ingredient in ingredients:
        if ingredient not in elements:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
