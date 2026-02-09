from ex0 import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "artifact"

    def play(self, game_state: dict) -> dict:
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
        print("ability_activated")
