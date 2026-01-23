class GardenError(Exception):
    """
    Base class for garden-related exceptions.
    """

    def __init__(self, message="A garden error has occured.") -> None:
        """
        Initialize GardenError with a default message.
        """
        super().__init__("GardenError: " + message)


class PlantError(GardenError):
    """
    This class inherit from GardenError
    Base class for plant-related exceptions.
    """

    def __init__(self, message="A plant error has occured.") -> None:
        """
        Initialise PlantError with a default message.
        """

        super().__init__("PlantError: " + message)


class GardenManager:
    """
    This class manage a garden with multiple plants.
    """

    def __init__(self) -> None:
        """
        Initialize the GardenManager with an empty garden.
        """
        self.garden = {}

    def add_plant(self, plant_name: str, water_level: int,
                  sunlight_hours: int) -> None:
        """
        Add a plant to the garden with its water level and sunlight hours.
        Raises PlantError for invalid inputs.

        Args:
            plant_name (str): The name of the plant.
            water_level (int): The water level of the plant (1-10).
            sunlight_hours (int): The sunlight hour required for the plant 2-10
        """
        if plant_name in self.garden.keys():
            raise GardenError("This plant is already in the garden.")
        elif plant_name == "":
            raise PlantError("Plant name cannot be empty!")
        elif not isinstance(plant_name, str):
            raise TypeError("TypeError: Invalid input for plant_name !")
        elif not isinstance(water_level, int):
            raise TypeError("TypeError: Invalid type for water level")
        elif not isinstance(sunlight_hours, int):
            raise TypeError("TypeError: Invalid type for sunlight hours")
        elif not (1 <= water_level <= 10):
            raise PlantError(f"Water level is invalid for {plant_name}")
        elif not (2 <= sunlight_hours <= 10):
            raise PlantError(f"Sunlight hours is invalid for {plant_name}")
        else:
            print(f"Added {plant_name} successfully !")
            self.garden[plant_name] = {
                "water_level": water_level, "sunlight_hours": sunlight_hours}

    def water_plant(self) -> None:
        """
        Water all plants in the garden by increasing their water level by 1.
        Raises GardenError if watering fails.
        """
        for plant in self.garden:
            self.garden[plant]["water_level"] += 1
            print(f"Watering {plant} - success")

    def check_plant_health(self) -> None:
        """
        Check the health of all plants in the garden.
        PlantError if any plant has invalid water level or sunlight hours.
        """
        for plant in self.garden.keys():
            if not (1 <= self.garden[plant]["water_level"] <= 10):
                raise PlantError(f"Invalid water_level for {plant}")
            if not (2 <= self.garden[plant]["sunlight_hours"] <= 12):
                raise PlantError(f"Invalid sunlight hours for {plant}")


def test_garden_management() -> None:
    """
    This function is a tester of the Garden Management System.
    It demonstrates adding plants, watering them, checking their health,
    and handling errors appropriately.
    """
    print("=== Garden Management System ===\n")
    manager = GardenManager()
    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 8, 5)
        manager.add_plant("lettuce", 10, 5)
        manager.add_plant("", 4, 6)
    except (PlantError, ValueError, TypeError) as e:
        print(e)

    print("\nWatering Plants...")
    try:
        print("Opening watering system")
        manager.water_plant()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

    print("Checking plant health...")
    try:
        manager.check_plant_health()
    except PlantError as e:
        print(e)

    print("\nTesting errors recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print("Caught", e)

    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
