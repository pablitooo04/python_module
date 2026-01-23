def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    This function check some data about the plant.

    Args:
        plant_name: (str)
        water_level: (int)
        sunlight_hours: (int)

    raise a ValueError if an information is not valid.
    """
    if plant_name == "":
        raise ValueError("plant_name must not be empty.")
    if not (1 <= water_level <= 10):
        raise ValueError("water_level must be between 1 and 10")
    if not (2 <= sunlight_hours <= 12):
        raise ValueError("sunlight_hours must be between 2 and 12")


def test_plant_checks() -> None:
    """
    This function is a tester of check_plant_health.
    It catch each error appropriately.
    """

    args = [
        ["tomato", 5, 5, "Testing good values..."],
        ["", 4, 6, "Testing empty plant name..."],
        ["carrot", 150, 7, "Testing bad water level..."],
        ["plant", 7, 150, "Testing bad sunlight hours..."]
    ]

    print("=== Garden Plant Health Checker ===\n")
    for arg in args:
        try:
            print(arg[3])
            check_plant_health(*(arg[:3]))
        except ValueError as e:
            print(e, end="\n\n")
        else:
            print(f"Plant {arg[0]} is fine !\n")

    print("All errors ")


if __name__ == "__main__":
    test_plant_checks()
