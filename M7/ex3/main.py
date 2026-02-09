from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity



def main() -> None:
    """
    Main function to demonstrate the Abstract Factory and Strategy patterns in a fantasy card game context.
    Configures the game engine with a fantasy card factory and an aggressive strategy, simulates a
    turn, and prints the results.
    
    Returns:
        None
    """
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    fantasy_factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print("Factory: FantasyCardFactory")
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", fantasy_factory.get_supported_types())
    print()

    print("Simulating aggressive turn...")
    engine = GameEngine()
    engine.configure_engine(fantasy_factory, strategy)
    enemy = CreatureCard("Enemy Player", 3, Rarity.LEGENDARY.value, 5, 5)
    engine.battlefield.append(enemy)

    Actions = engine.simulate_turn()
    print("Actions:", Actions)
    print("Game Report:", engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()