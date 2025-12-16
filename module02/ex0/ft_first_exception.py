def check_temperature(temp_str: str) -> int:
    try:
        temp_int: int = int(temp_str)
        if temp_int < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
            raise Exception
        if temp_int > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
            raise Exception
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    except Exception:
        pass
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return temp_int


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    good_input: str = "25"
    bad_input: str = "abc"
    extreme_min: str = "-50"
    extreme_max: str = "100"

    print(f"\nTesting good temperature: {good_input}")
    check_temperature(good_input)

    print(f"\nTesting bad temperature: {bad_input}")
    check_temperature(bad_input)

    print(f"\nTesting extreme min temperature: {extreme_min}")
    check_temperature(extreme_min)

    print(f"\nTesting extreme max temperature: {extreme_max}")
    check_temperature(extreme_max)


# test_temperature_input()
