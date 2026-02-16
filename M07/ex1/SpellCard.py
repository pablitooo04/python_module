from ex0.Card import Card


class SpellCard(Card):
    """
    A class representing a spell card in a card game,
    inheriting from the base Card class.
    """
    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """
        Initializes a SpellCard with the given attributes.
        Args:
            name (str): The name of the spell card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card.
            effect_type (str): The type of effect the spell card has.
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "spell"

    def play(self, game_state: dict) -> dict:
        """
        Simulates playing the spell card in a game.
        Args:
            game_state (dict): A dictionary representing the
            current state of the
            game, expected to contain keys "active" (bool) and "mana" (int).
        Returns:
            dict: A dictionary containing the details of the card play action,
            or a dictionary with None values if the card cannot be played.
        """
        if (game_state.get("active", False) and
                self.is_playable(game_state.get("mana", 0))):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Spell effect of type: " + self.effect_type
            }

        else:
            return {
                'card_played': None,
                'mana_used': 0,
                'effect': None
            }

    def resolve_effect(self, targets: list) -> dict:
        """
        Simulates resolving the spell card's effect on a list of targets.
        Args:
            targets (list): A list of target objects
            that the spell's effect will
            be applied to. Each target is expected to have a 'name' attribute.
        Returns:
            dict: A dictionary containing the details of the effect resolution.
        """
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': [target.name for target in targets]
        }
