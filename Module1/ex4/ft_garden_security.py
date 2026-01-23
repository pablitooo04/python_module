class SecurePlant:
    """
    Represents a plant with a name, height in cm, and age in days.
    This class handles corrupted args.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        This method init the object

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: int) -> None:
        """
        This method sets the height of the plant.

        Args:
            value (int): The height to set in centimeters.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
        else:
            self.__height = value
            print(f"Height succesfully set to {value}")

    def set_age(self, value: int) -> None:
        """
        This method sets the age of the plant.

        Args:
            value (int): The age to set in days.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
        else:
            self.__age = value
            print(f"Age successfully set to {value}")

    def get_height(self) -> int:
        """
        This method returns the secure height of the plant
        """
        return self.__height

    def get_age(self) -> int:
        """
        This method returns the secure age of the plant.
        """
        return self.__age
