from ex0 import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'game_state': game_state
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': 15,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'damage_blocked': 12,
            'still_alive': (100 - incoming_damage) > 0
        }

    def get_combat_stats(self) -> dict:
        return {"combat": True}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        target_names = [target.name for target in targets]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': 3, 'total_mana': 7}

    def get_magic_stats(self) -> dict:
        return {"mana": True}
