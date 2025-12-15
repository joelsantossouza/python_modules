def ft_count_harvest_recursive(start: int = 1, max_days: int = 0) -> None:
    if start == 1:
        max_days = int(input("Days until harvest: "))
    if start > max_days:
        print("Harvest time!")
        return
    print(f"Day {start}")
    ft_count_harvest_recursive(start + 1, max_days)
