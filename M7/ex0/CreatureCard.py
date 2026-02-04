from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def play(self, game_state: dict) -> dict:
        if game_state.get("active", False) and self.is_playable(game_state.get("mana", 0)):
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
        info = {
            'type': self.type,
            'attack': self.attack,
            'health': self.health
        }

        return super().get_card_info() | info
