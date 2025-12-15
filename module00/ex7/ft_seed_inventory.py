def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit_msg: str = f" seeds: {quantity} packets available"
    elif unit == "grams":
        unit_msg: str = f" seeds: {quantity} grams total"
    elif unit == "area":
        unit_msg: str = f" seeds: covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(seed_type.capitalize() + unit_msg)
