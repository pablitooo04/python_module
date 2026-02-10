from ex0.Card import Card


class CreatureCard(Card):
    """A class representing a creature card in a card game."""
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        """
        Initializes a CreatureCard with the given attributes.
        Args:
            name (str): The name of the creature card.
            cost (int): The mana cost to play the card.
            rarity (str): The rarity level of the card.
            attack (int): The attack value of the creature.
            health (int): The health value of the creature.
        Raises:
            ValueError: If attack or health is not a
            positive integer.
        """
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack < 1:
            raise ValueError("Error: attack must be a positive int!")
        if not isinstance(cost, int) or cost < 1:
            raise ValueError("Error: health must be a positive int!")
        self.attack = attack
        self.health = health
        self.type = "creature"

    def play(self, game_state: dict) -> dict:
        """
        Simulates playing the creature card in a game. If the game state
        indicates that the card is active and the player has enough mana,
        returns a dictionary containing the details of the card play action.
        Args:
            game_state (dict): A dictionary representing the
            current state of the game, expected to contain keys
            "active" (bool) and "mana" (int)
        Returns:
            dict: A dictionary containing the details of the card play action,
            or a dictionary with None values if the card cannot be played.
        """
        if (game_state.get("active", False) and
                self.is_playable(game_state.get("mana", 0))):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'
            }
        return {
            'card_played': None,
            'mana_used': 0,
            'effect': None
        }

    def attack_target(self, target: Card) -> dict:
        """
        Simulates an attack action against a target card.
        Args:
            target (Card): The target of the attack, expected to have a 'name'
            attribute and a 'health' attribute that can be reduced
            by the attack.
        Returns:
            dict: A dictionary containing the details of the attack action
        """
        target.health -= self.attack
        if target.health < 0:
            target.health = 0

        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': target.attack,
            'combat_resolved': target.health == 0
        }

    def get_card_info(self) -> dict:
        """
        Returns a dictionary containing the information about the
        creature card.
        Returns:
            dict: A dictionary containing the card's name, cost, rarity,
            type, attack, and health.
        """
        info = {
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        }

        return super().get_card_info() | info
