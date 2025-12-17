def garden_operations(error: str) -> None:
    if error == "ValueError":
        int("non-numeric string")
    elif error == "ZeroDivisionError":
        print(42 / 0)
    elif error == "FileNotFoundError":
        open("unexisting_file")
    elif error == "KeyError":
        dictionary = {}
        dictionary["Invalid_key"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    print("\nTesting ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as error:
        print(f"[Caught ValueError] - {error}")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as error:
        print(f"[Caught ZeroDivisionError] - {error}")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as error:
        print(f"[Caught FileNotFoundError] - {error}")

    print("\nTesting KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as error:
        print(f"[Caught KeyError] - {error}")

    print("\nTesting multiples errors together...")
    error_name: str = "KeyError"
    try:
        garden_operations(error_name)
    except (KeyError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully")


# test_error_types()
