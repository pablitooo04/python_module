class Plant:
    """
    Represents a plant with a name, height in cm, and age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initializes a Plant object.
        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in centimeters.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    cactus = Plant("Cactus", 20, 50)
    sunflower = Plant("Sunflower", 30, 90)
    rose = Plant("Rose", 40, 60)

    print("=== Garden Plant Registry ===")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
