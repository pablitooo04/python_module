from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy

class GameEngine:
    def configure_engine(self, factory: CardFactory, strategy: GameStrategy) -> None:
        """
        Configures the game engine with a specific card factory and strategy.
        Initializes the player's hand and battlefield based on the factory's 
        output.
        Args:
            factory (CardFactory): The card factory to use for creating cards.
            strategy (GameStrategy): The strategy to use for simulating turns.
        """
        self.factory = factory
        self.strategy = strategy

        self.hand = self.factory.create_themed_deck(3)["deck"]
        self.battlefield = [self.factory.create_creature() for _ in range(2)]

        self.strategy_used = strategy.get_strategy_name()
        self.total_damage = 0
        self.turns_simulated = 0
        self.cards_created = 0

    def simulate_turn(self) -> dict:
        """
        Simulates a single turn of the game using the configured strategy.
        Executes the strategy's turn logic and updates the engine's status
        based on the actions taken during the turn.
        Returns:
            dict: A summary of the actions taken during the turn, including:
                - "cards_played": List of card names played.
                - "mana_used": Total mana spent.
                - "targets_attacked": List of target names attacked.
                - "damage_dealt": Total damage dealt to enemy targets.
        """
        action = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += action["damage_dealt"]
        self.cards_created = len(self.hand) + len(self.battlefield)
        return action

    def get_engine_status(self) -> dict:
        """
        Returns the current status of the game engine, including the number of turns simulated,
        the strategy used, total damage dealt, and the number of cards created.
        Returns:
            dict: A dictionary containing the current status of the game engine.
        """
        engine_status = {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy_used,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
        return engine_status