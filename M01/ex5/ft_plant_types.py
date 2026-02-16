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

    def grow(self) -> None:
        """
        Makes the plant grow, increasing its size
        """
        self.height += 5

    def increase_age(self) -> None:
        """
        Makes the plant older.
        """
        self.age += 1


class Flower(Plant):
    """
    Represents a flower.
    """

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initializes a Flower object.
        Args:
            name (str): The name of the flower.
            height (int): The height of the flower in centimeters.
            age (int): The age of the flower in days.
            color (str): The color of the flower.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """
        Makes the flower bloom.
        """
        print(f"{self.name} is blooming beautifully!")

    def info(self) -> None:
        """
        Print some info about the flower.
        """
        print(f"{self.name} (Flower): {self.height}cm, ", end="")
        print(f"{self.age} days, Color: {self.color}")


class Tree(Plant):
    """
    Represents a tree.
    """

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """
        Calculates the shade provided by the tree.
        """
        shade = (self.trunk_diameter * self.height)
        print(f"{self.name} provides {shade} square meters of shade")

    def info(self) -> None:
        """
        Print some info about the tree.
        """
        print(f"{self.name} (Tree): {self.height}cm,", end="")
        print(f" {self.age} days, Trunk Diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    """
    Represents a vegetable.
    """

    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initializes a Vegetable object.
        Args:
            name (str): The name of the vegetable.
            height (int): The height of the vegetable in centimeters.
            age (int): The age of the vegetable in days.
            harvest_season (str): The season when the vegetable is harvested.
            nutritional_value (str): The nutritional value of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_nutrition(self) -> None:
        """
        Displays the nutritional value of the vegetable.
        """
        print(f"{self.name} is rich in {self.nutritional_value.lower()}")

    def info(self) -> None:
        """
        Print some info about the vegetable.
        """
        print(f"{self.name} (Vegetable): {self.height}cm, ", end="")
        print(f"{self.age} days, Harvest Season:  ", end="")
        print(f"{self.harvest_season},Nutritional Value: ")
        print(self.nutritional_value)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "Red")
    tulip = Flower("Tulip", 20, 15, "Yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    carrot = Vegetable("Carrot", 30, 80, "Autumn", "Vitamin A")
    tomato = Vegetable("Tomato", 80, 90, "Summer", "Vitamin C")

    rose.info()
    rose.bloom()

    oak.info()
    oak.produce_shade()

    tomato.info()
    tomato.get_nutrition()
