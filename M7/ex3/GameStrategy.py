from abc import ABC, abstractmethod

class GameStrategy(ABC):
    """Abstract base class for game strategies. 
    Defines the interface for executing a turn, 
    getting the strategy name,"""
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        ...
    
    @abstractmethod
    def get_strategy_name(self) -> str:
        ...
    
    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        ...