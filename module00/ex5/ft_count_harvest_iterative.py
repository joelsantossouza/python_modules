def ft_count_harvest_iterative() -> None:
    days_to_harvest: int = int(input("Days until harvest: "))
    day: int = 1
    while (day <= days_to_harvest):
        print(f"Day {day}")
        day += 1
    print("Harvest time!")
