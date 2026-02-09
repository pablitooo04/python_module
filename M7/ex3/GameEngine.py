from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        self.hand = self.factory.create_themed_deck(3)["deck"]
        self.battlefield = [self.factory.create_creature() for _ in range(2)]

        self.strategy_used = strategy.get_strategy_name()
        self.total_damage = 0
        self.turns_simulated = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        action = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += action["damage_dealt"]

        return action

    def get_engine_status(self) -> dict:
        engine_status = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy_used,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
        return engine_status