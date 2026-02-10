from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card
from random import random

class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, id_card: str, rating: int):
        super().__init__(name, 0, "Special")
        self.id_card = id_card
        self.rating = rating
        self.wins = 0
        self.losses = 0
    
    def play(self, game_state: dict) -> dict:
        if (game_state.get("active", False)):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
    
    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': 15,
            'combat_type': 'melee'
        }
    
    def get_tournament_stats(self) -> dict:
        return {'game_played': self.wins + self.losses}

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 12,
            'still_alive': (100 - incoming_damage) > 0
        }

    def get_combat_stats(self) -> dict:
        return {"combat": True}

    def calculate_rating(self) -> int:
        self.rating = abs(self.wins - self.losses) * random()
        return int(self.rating)

    def update_wins(self, wins: int) -> None:
        self.wins = wins
    
    def update_losses(self, losses: int) -> None:
        self.losses = losses
    
    def get_rank_info(self) -> dict:
        return {"wins": self.wins,
                "losses": self.losses,
                "rate": self.calculate_rating()}