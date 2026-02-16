from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):
    """Abstract base class for combat-capable cards."""
    @abstractmethod
    def attack(self, target: Card) -> dict:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        ...
