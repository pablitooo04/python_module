from ex4.TournamentCard import TournamentCard
from random import randint


class TournamentPlatform:
    """A platform to manage a tournament of cards, allowing
    players to register their cards, create matches, and track
    their performance."""

    def __init__(self) -> None:
        """
        Initializes the tournament platform with an empty list of players,
        a score of 0 for both players, and a count of matches played.
        """
        self.tournament_players = []
        self.score = [0, 0]
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Registers a card for the tournament. Ensures that the card is a valid
        TournamentCard and that there are not already two players registered.
        Args:
            card (TournamentCard): The card to be registered for the tournament
        Returns:
            str: A confirmation message indicating successful registration.
        Raises:
            ValueError: If the card is not a TournamentCard or if there are
            already two players registered in the tournament.

        """
        if not isinstance(card, TournamentCard):
            raise ValueError("card must be a Tournament Card!")
        if len(self.tournament_players) == 2:
            raise ValueError("Too much players in this tournament!")
        else:
            self.tournament_players.append(card)
            return f"{card.name} has been registered for the tournament!"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Creates a match between two registered cards and determines the winner
        based on a random outcome. Updates the wins and losses for each card
        accordingly and returns the match results.
        Args:
            card1_id (str): The ID of the first card.
            card2_id (str): The ID of the second card.
        Returns:
            dict: A dictionary containing the match results.
        Raises:
            ValueError: If there are not exactly two players
            registered in the tournament.
        """
        if len(self.tournament_players) != 2:
            raise ValueError("Add more cards to create a match!")
        else:
            n1, n2 = randint(0, 3), randint(0, 3)
            if n1 > n2:
                winner = self.tournament_players[0]
                loser = self.tournament_players[1]
                winner.update_wins(winner.wins + 1)
                loser.update_losses(loser.losses + 1)
                winner_id, winner_rating = card1_id, winner.rating
                loser_id, loser_rating = card2_id, loser.rating
            else:
                winner = self.tournament_players[1]
                loser = self.tournament_players[0]
                winner.update_wins(winner.wins + 1)
                loser.update_losses(loser.losses + 1)
                winner_id, winner_rating = card2_id, winner.rating
                loser_id, loser_rating = card1_id, loser.rating
            self.match_played += 1
            return {
                'winner': winner_id,
                'loser': loser_id,
                'winner_rating': winner_rating,
                'loser_rating': loser_rating
            }

    def get_leaderboard(self) -> list:
        """
        Generates a leaderboard of the registered players in the tournament,
        sorted by their rating in descending order.
        Returns:
            list: A list of strings representing the leaderboard.
        """
        leaderboard = []
        podium = sorted(self.tournament_players,
                        key=lambda x: x.rating, reverse=True)
        for i in range(len(podium)):
            player = podium[i]
            line = f"{i + 1}. {player.name} "
            line += f"- Rating: {player.rating} "
            line += f"({player.wins}-{player.losses})"
            leaderboard.append(line)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        """
        Generates a report summarizing the current state of the tournament,
        Returns:
            dict: A dictionary containing the tournament statistics.
        """
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
            'platform_status': "active"
        }
