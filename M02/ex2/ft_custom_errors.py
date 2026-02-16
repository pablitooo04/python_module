class GardenError(Exception):
    """
    Base class for garden-related exceptions.
    """

    def __init__(self, message="A GardenError has occured.") -> None:
        """
        Initialize GardenError with a default message.
        """

        super().__init__(message)


class PlantError(GardenError):
    """
    This class inherit from GardenError
    Base class for plant-related exceptions.
    """

    def __init__(self, message="A PlantError has occured.") -> None:
        """
        Initialise PlantError with a default message.
        """

        super().__init__(message)


class WaterError(GardenError):
    """
    This class inherit from GardenError
    Base class for water-related exceptions.
    """

    def __init__(self, message="A WaterError has occured.") -> None:
        """
        Initialise WaterError with a default message.
        """

        super().__init__(message)


def testing_errors() -> None:
    """
    Test the custom garden-related exceptions.
    """
    print("=== Testing Custom Garden Errors ===\n")

    try:
        raise GardenError()
    except GardenError:
        print("Caught garden error !")

    try:
        raise PlantError()
    except PlantError:
        print("Caught plant error !")

    try:
        raise WaterError()
    except WaterError:
        print("Caught water error !\n")

    print("All custom errors tested successfully!")


if __name__ == "__main__":
    testing_errors()
