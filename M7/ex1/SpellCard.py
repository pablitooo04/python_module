from ex0 import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.type = "spell"

    def play(self, game_state: dict) -> dict:
        if (game_state.get("active", False) and
                self.is_playable(game_state.get("mana", 0))):
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': self.cost
            }

        else:
            return {
                'card_played': None,
                'mana_used': 0,
                'effect': None
            }

    def resolve_effect(self, targets: list) -> dict:
        print("resolved_effect")
