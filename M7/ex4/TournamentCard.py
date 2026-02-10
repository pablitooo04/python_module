from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from ex0.Card import Card


class TournamentCard(Card, Combatable, Rankable):
    """Represents a card that can be used in a tournament setting,"""
    def __init__(self, name: str, id_card: str, rating: int) -> None:
        """
        Initializes a TournamentCard with the given name, ID, and rating.
        The card is initialized with a cost of 0 and a rarity of "Special".
        Args:
            name (str): The name of the card.
            id_card (str): The unique identifier for the card.
            rating (int): The initial rating of the card.
        """
        super().__init__(name, 0, "Special")
        self.id_card = id_card
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """
        Simulates playing the card in a game.
        If the game state indicates that the card is active,
        returns a dictionary
        Args:
            game_state (dict): A dictionary representing the current
            state of the game.
        Returns:
            dict: A dictionary containing the details of the card play action
        """
        if (game_state.get("active", False)):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }

    def attack(self, target) -> dict:
        """
        Simulates an attack action against a target. Returns a dictionary
        containing the details of the attack.
        Args:
            target: The target of the attack, expected to have a
            'name' attribute.
        Returns:
            dict: A dictionary containing the details of the attack action.
        """
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': 15,
            'combat_type': 'melee'
        }

    def get_tournament_stats(self) -> dict:
        """
        Returns a dictionary containing the tournament statistics for the card.
        Returns:
            dict: A dictionary containing the tournament statistics
            for the card.
        """
        return {'game_played': self.wins + self.losses}

    def defend(self, incoming_damage: int) -> dict:
        """
        Simulates a defense action against incoming damage. Returns a
        dictionary containing the details of the defense.
        Args:
            incoming_damage (int): The amount of damage incoming to the card.
        Returns:
            dict: A dictionary containing the details of the defense action.
        """
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 12,
            'still_alive': (100 - incoming_damage) > 0
        }

    def get_combat_stats(self) -> dict:
        """
        Returns a dictionary containing the combat statistics for the card
        Returns:
            dict: A dictionary containing the combat statistics for the card.
        """
        return {"combat": True}

    def calculate_rating(self) -> int:
        """
        Calculates the current rating of the card based on its wins and losses.
        Each win increases the rating by 16 points, and each loss
        decreases it by 16
        points. Returns the current rating as an integer.
        Returns:
            int: The current rating of the card.
        """
        return int(self.rating)

    def update_wins(self, wins: int) -> None:
        """
        Updates the number of wins for the card and adjusts
        the rating accordingly. Each win increases the rating by 16 points.
        Args:
            wins (int): The new total number of wins for the card.
        """
        self.wins = wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        """
        Updates the number of losses for the card and adjusts the
        rating accordingly.
        Each loss decreases the rating by 16 points.
        Args:
            losses (int): The new total number of losses for the card.
        """
        self.losses = losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        """
        Returns a dictionary containing the current wins, losses,
        and calculated rating for the card.
        Returns:
            dict: A dictionary containing the current wins,
            losses, and calculated rating for the card.
        """
        return {"wins": self.wins,
                "losses": self.losses,
                "rate": self.calculate_rating()}
