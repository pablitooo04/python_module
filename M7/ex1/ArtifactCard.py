from ex0 import Card


class ArtifactCard(Card):
    """A class representing an artifact card in a card game."""
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        """
        Initializes an ArtifactCard with the given attributes.
        Args:
            name (str): The name of the artifact card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card.
            durability (int): The durability value of the artifact.
            effect (str): The effect description of the artifact.
        Raises:
            ValueError: If durability is not a positive integer.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "artifact"

    def play(self, game_state: dict) -> dict:
        """
        Simulates playing the artifact card in a game.
        Args:
            game_state (dict): A dictionary representing the
            current state of the game.
        Returns:
            dict: A dictionary containing the details of the card play action.
        """
        if (game_state.get("active", False) and
                self.is_playable(game_state.get("mana", 0))):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.effect
            }
        return {
            'card_played': None,
            'mana_used': 0,
            'effect': None
        }

    def activate_ability(self) -> dict:
        """
        Simulates activating the artifact's ability. Returns a dictionary
        containing the details of the ability activation.
        """
        print("ability_activated")
