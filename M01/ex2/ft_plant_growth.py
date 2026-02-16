class Plant:
    """
    Represents a plant with a name, height in cm, and age in days.
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        This method init the object
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """
        Makes the plant grow, increasing its size
        """
        self.height += 1

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
        print(f"Name: {self.name}", end="")
        print(f" Height: {self.height}", end="")
        print(f" Age: {self.age}")
        print("====================")


if __name__ == "__main__":
    sunflower = Plant("Sunflower", 15, 10)
    cactus = Plant("Cactus", 20, 50)
    rose = Plant("Rose", 30, 40)
    plants = [sunflower, cactus, rose]
    print("=== Starting Week Simulation ===")
    for day in range(1, 8):
        print(f"\n--- Day {day} ---")
        for plant in plants:
            plant.grow()
            plant.increase_age()
            plant.get_info()
    print("\n=== End of Week Simulation ===")
