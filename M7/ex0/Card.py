from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        info: dict = {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

        return info

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost
