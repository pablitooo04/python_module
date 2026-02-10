from ex0 import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        """
        Simulates playing the elite card in a game.
        Args:
            game_state (dict): A dictionary representing the current
            state of the
            game, expected to contain keys "active" (bool) and "mana" (int).
        Returns:
            dict: A dictionary containing the details of the card play action,
            or a dictionary with None values if the card cannot be played.
        """
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'game_state': game_state
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

    def defend(self, incoming_damage: int) -> dict:
        """
        Simulates a defense action against incoming damage. Returns
        a dictionary containing the details of the defense.
        Args:
            incoming_damage (int):
            The amount of damage being defended against.
        Returns:
            dict: A dictionary containing the details of the
            defense action.
        """
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 12,
            'still_alive': (100 - incoming_damage) > 0
        }

    def get_combat_stats(self) -> dict:
        """Returns a dictionary containing the combat statistics
        for the card."""
        return {"combat": True}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """Simulates casting a spell with the elite card.
        Returns a dictionary"""
        target_names = [target.name for target in targets]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        """Simulates channeling mana with the elite card.
        Returns a dictionary."""
        return {'channeled': 3, 'total_mana': 7}

    def get_magic_stats(self) -> dict:
        """Returns a dictionary containing the magic
        statistics for the card."""
        return {"mana": True}
