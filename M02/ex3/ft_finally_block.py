def water_plants(plant_list: list) -> None:
    """
    This function waters a list of plants.
    Args:
        plant_list: (list) A list of plant names (str).
    """
    print("Testing normal watering...")
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise (ValueError)
            else:
                print(f"Watering {plant}")
    except ValueError:
        print(f"Error: Cannot water {str(plant)} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed successfully!\n")

    plant_list = ["tomato", None, "carrots"]
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")
