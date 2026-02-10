from ex4.TournamentCard import TournamentCard
from random import randint


class TournamentPlatform:
    def __init__(self) -> None:
        self.tournament_players = []
        self.score = [0, 0]
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("card must be a Tournament Card!")
        if len(self.tournament_players) == 2:
            return "Too much players in this tournament!"
        else:
            self.tournament_players.append(card)

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if len(self.tournament_players) != 2:
            raise ValueError("Add more cards to create a match!")
        else:
            n1, n2 = randint(0, 3), randint(0, 3)
            if n1 > n2:
                winner = self.tournament_players[0]
                looser = self.tournament_players[1]
                winner.update_wins(winner.wins + 1)
                looser.update_losses(winner.losses + 1)
                winner_id, winner_rating = card1_id, winner.rating
                looser_id, looser_rating = card1_id, looser.rating
            else:
                winner = self.tournament_players[1]
                looser = self.tournament_players[0]
                winner.update_wins(winner.wins + 1)
                looser.update_losses(winner.losses + 1)
                winner_id, winner_rating = card1_id, winner.rating
                looser_id, looser_rating = card1_id, looser.rating
            self.match_played += 1
            return {
                'winner': winner_id,
                'looser': looser_id,
                'winner_rating': winner_rating,
                'looser_rating': looser_rating
            }

    def get_leaderboard(self) -> list:
        leaderboard = []
        for i in range(len(self.tournament_players)):
            player = self.tournament_players[i]
            line = f"{i + 1}. {player.name} "
            line += f"({player.wins}-{player.losses})"
            leaderboard.append(line)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        if len(self.tournament_players) == 0:
            avg = None
        elif len(self.tournament_players) == 1:
            avg = self.tournament_players[0].rating
        else:
            avg = sum(_.rating for _ in self.tournament_players) / 2

        return {
            'total_cards': len(self.tournament_players),
            'matches_played': self.match_played,
            'avg_rating': avg,
            'plateform_status': "active"
        }
