"(temp,20)"class Plant0
    """
    Represents a plant with a name, height in cm, and age in days.
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
        self.height = height
        self.age = age

    def grow(self):
        """
        Makes the plant grow, increasing its size
        """
        self.height += 5

    def increase_age(self):
        """
        Makes the plant older.
        """
        self.age += 1

    def get_info(self):
        """
        Print some info about the plant.
        """
        print("=== Data Plants ===")
        print(f"Name: {self.name}")
        print(f"Height: {self.height}")
        print(f"Age: {self.age}")
        print("====================")


def create_plant_factory(name: str, height: int, age: int) -> Plant:
    """
    Factory function to create a Plant instance.
    Args:
        name (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    Returns:
        Plant: A new Plant instance.
    """
    print("Created: Rose (25cm, 30 days)")
    return Plant(name, height, age)


if __name__ == "__main__":
    plants = [
        create_plant_factory("Sunflower", 15, 10),
        create_plant_factory("Cactus", 20, 50),
        create_plant_factory("Rose", 30, 40),
        create_plant_factory("Tulip", 12, 5),
        create_plant_factory("Poppy", 18, 7),
    ]
