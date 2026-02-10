from ex4.TournamentCard import TournamentCard
from random import random, randint

class TournamentPlatform():
    def __init__(self) -> None:
        self.tournament_players = []
        self.score = [0, 0]
        self.match_played

    def register_card(self, card: TournamentCard) -> str:
        if len(self.tournament_players) == 2:
            return "Too much players in this tournament!"
        else:
            self.tournament_players.append(card)

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if len(self.tournament_players) != 2:
            return {'combat_executed': False}
        else:
            n1, n2 = randint(0, 3), randint(0, 3)
            return {
                'combat_executed': True,
                'score': [n1, n2],
                
                }

    def get_leaderboard(self) -> list:
        ...
    def generate_tournament_report(self) -> dict:
        if len(self.tournament_players) == 0:
            avg = None
        elif len(self.tournament_players) == 1:
            avg = self.tournament_players[0].rating
        else:
            avg = sum(_.rate for _ in self.tournament_players) / 2
        
        return {
            'total_cards': len(self.total_cards),
            'matches_played': self.match_played,
            'avg_rating': avg,
            'plateform_status': True
        }