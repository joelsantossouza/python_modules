def ft_harvest_total() -> None:
    total: int = 0
    day: int = 1
    while (day <= 3):
        total += int(input(f"Day {day} harvest: "))
        day += 1
    print(f"Total harvest: {total}")
