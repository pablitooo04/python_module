class Plant:
    """
    A class which can represent any Plant.
    """

    def __init__(self, name: str, height: int) -> None:
        """
        Initialise the plant with:
        Args :
            name -> str
            height in cm -> int
        """
        self.name = name
        self.height = height

    def grow(self) -> None:
        """
        This method makes the plant grow, increasing his height
        """
        self.height += 10
        print(f"{self.name} grew, it is {self.height}cm tall.")

    def print_data(self) -> None:
        """
        This method print some data about the plant.
        """
        print("===== Plant Data =====")
        print(f"Name : {self.name}")
        print(f"Height : {self.height}cm")


class FloweringPlant(Plant):
    """
    This class inherits from the Plant class.
    This class represents a flower.
    """

    def __init__(self, name: str, height: int, color: str,
                 is_blooming: bool) -> None:
        """
        This method initialise the object.

        Args :
            name -> str
            height in cm -> int
            color -> str
            is blooming -> bool
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming

    def print_data(self) -> None:
        """
        This method print some data about the plant.
        """
        super().print_data()
        print(f"Color {self.color}")
        if self.is_blooming:
            print("Blooming : Yes")
        else:
            print("Blooming : No")


class PrizeFlower(FloweringPlant):
    """
    This class inherits from the FloweringPlant class.
    This class represents a plant which have a score.
    """

    def __init__(self, name: str, height: int, color: str, is_blooming: bool,
                 score: int) -> None:
        """
        This method initialise the object.

        Args:
            name -> str
            height in cm -> int
            color -> str
            is blooming -> bool
            score -> int
        """
        super().__init__(name, height, color, is_blooming)
        self.score = score

    def get_score(self) -> int:
        """
        This method return the score of the flower.
        """
        return (self.score)

    def print_data(self) -> None:
        super().print_data()
        print(f"Score :{self.score}")


class Garden:
    """
    A class which can represent any Garden.
    """

    def __init__(self, name: str) -> None:
        """
        Initialise the garden with:
        Args :
            name -> str
        """
        self.plants = []
        self.name = name
        self.score = 0

    def add_plant(self, plant: Plant) -> None:
        """
        This method add a new plant to the garden.

        Args:
            plant -> Plant
        """
        print(f"---Added {plant.name} to {self.name}'s Garden---")
        self.plants += [plant]
        if isinstance(plant, PrizeFlower):
            self.score += plant.score

    def grow(self) -> None:
        """
        This method makes the plant grow, increasing his height
        """
        print("===== Growing Plants =====")
        for plant in self.plants:
            plant.grow()

    def get_score(self) -> int:
        """
        Return the total score of each plants in the garden.
        """
        return self.score


class GardenManager:
    """
    A class which can handle any group of Gardens
    """
    all_gardens, garden_networks = [], {}

    @classmethod
    def add_garden(cls, garden: Garden) -> None:
        """
        This method add the garden to a list which represent all the gardens.

        Args:
            garden -> Garden
        """
        cls.all_gardens += [garden]

    @classmethod
    def create_garden_network(cls, name: str, gardens: list) -> None:
        """
        This class method create a garden network.

        Args:
            name -> str
            gardens -> list
        """
        if name in cls.garden_networks.keys():
            print(f"Error : {name} is already a garden network.")
        cls.garden_networks[name] = gardens
        print(f"~~~Garden network {name} created.~~~")

    @classmethod
    def search_garden_network(cls, name: str) -> None:
        """
        This class method search for a garden network by its name.

        Args:
            name -> str
        """
        if name in cls.garden_networks.keys():
            print(f"{name} is a garden network.")
            print("It contain : |", end="")
            for garden in cls.garden_networks[name]:
                print(f" {garden.name} |", end="")
            print("")

    class GardenStats:
        """
        A nested class which can print some statistics about the gardens.
        """
        @classmethod
        def print_stats(cls) -> None:
            """
            This class method can print some statistics about the gardens.
            """
            plants = []
            print("===== Garden Stats =====")
            print("Gardens scores :", end="")
            for garden in GardenManager.all_gardens:
                print(f" {garden.name}: {garden.get_score()}", end="")
            print("")
            print(f"Gardens managed : {len(GardenManager.all_gardens)}")
            for garden in GardenManager.all_gardens:
                for plant in garden.plants:
                    plants.append(plant.height)

            print(f"Average height : {cls.average(plants)}")

        @staticmethod
        def average(heights: list) -> int:
            """
            This static method calculate the average of all the int in the tab
            Args:
                heights -> list
            Returns:
                int -> average of the heights
            """
            if heights:
                return (sum(heights)//len(heights))
            else:
                return 0


def tester() -> None:
    # plantes
    plante1 = Plant("rose", 10)
    plante2 = FloweringPlant("Saucisse", 10, "rouge", True)
    plante3 = PrizeFlower("requin", 1, "rouge", True, 100)
    plante4 = PrizeFlower("voiture", 1, "verte", True, 50)

    plante1.print_data()
    print("")
    plante2.print_data()
    print("")
    plante3.print_data()
    print("")

    # garden
    garden1 = Garden("Pablo")
    garden2 = Garden("Bob")

    # add plants to garden
    garden1.add_plant(plante1)
    garden1.add_plant(plante2)
    garden1.add_plant(plante3)
    garden1.add_plant(plante4)
    garden2.add_plant(PrizeFlower("parapluie", 100, "blue", False, 120))
    print("")

    # grow plants
    garden1.grow()
    garden2.grow()
    print("")

    # garden manager
    GardenManager.add_garden(garden1)
    GardenManager.add_garden(garden2)
    GardenManager.GardenStats.print_stats()
    print("")

    # create garden network
    GardenManager.create_garden_network("fields1", [garden1, garden2])
    GardenManager.search_garden_network("fields1")
