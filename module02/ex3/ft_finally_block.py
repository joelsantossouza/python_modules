def water_plants(plant_list: list[str]) -> None:
    """
    Water all plants on a givin list
    """
    print("Opening watering system")
    success: bool = False
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
        success = True
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests specific cases
    """
    print("\nTesting normal watering...")
    good_list: list[str] = [
        "tomato",
        "lettuce",
        "carrots",
    ]
    water_plants(good_list)

    print("\nTesting with error...")
    bad_list: list[str] = [
        "tomato",
        None
    ]
    water_plants(bad_list)


# if __name__ == "__main__":
#     print("=== Garden Watering System ===")
#     test_watering_system()
#     print("\nCleanup always happens, even with errors!")
