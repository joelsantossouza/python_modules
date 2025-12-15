def ft_plot_area() -> None:
    length: str = input("Enter length: ")
    width: str = input("Enter width: ")
    total: int = (0 if length == "" else int(length)) * (0 if width == "" else int(width))
    print(f"Plot area: {area}")
