from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    """
    Enumeration for card rarity levels.
    """
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class Card(ABC):
    """
    Abstract base class for all card types in the game.
    """
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initializes a card with the given name, cost, and rarity.
        Args:
            name (str): The name of the card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card, expected to be one of
            the values defined in the Rarity enum.
        Raises:
            ValueError: If the name is not a non-empty string, or if the
            costis not a non-negative integer, or if the rarity is not a
            valid value from the Rarity enum.
        """
        if not isinstance(name, str) or name == "":
            raise ValueError("Error: name must be a non-empty str!")
        self.name = name
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Error cost must be an int!")
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Abstract method to simulate playing the card in a game. Must be
        implemented by subclasses.
        Args:
            game_state (dict): A dictionary representing the
            current state of the game.
        Returns:
            dict: A dictionary containing the details of the
            card play action.
        """
        pass

    def get_card_info(self) -> dict:
        """
        Returns a dictionary containing the basic information about the card,
        including its name, cost, and rarity.
        Returns:
            dict: A dictionary containing the card's name, cost, and rarity.
        """
        info: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

        return info

    def is_playable(self, available_mana: int) -> bool:
        """
        Determines if the card can be played based on the available mana.
        Args:
            available_mana (int): The amount of mana currently available
            to the player.
        Returns:
            bool: True if the card can be played
        """
        return available_mana >= self.cost
