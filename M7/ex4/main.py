from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    """
    Main function to demonstrate the functionality of
    the TournamentCard and TournamentPlatform classes.
    """
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    try:
        player_1 = TournamentCard("Fire Dragon", "dragon_001", 1200)
    except ValueError as exc:
        print(exc)
    else:
        print(f"{player_1.name} (ID: {player_1.id_card})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {player_1.rating}")
        print("- Record: 0-0")

    print()

    try:
        player_2 = TournamentCard("Ice wizard", "wizard_001", 1150)
    except ValueError as exc:
        print(exc)
    else:
        print(f"{player_2.name} (ID: {player_2.id_card})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {player_2.rating}")
        print("- Record: 0-0")

    print()
    print("Creating tournament match...")
    tournament = TournamentPlatform()
    tournament.register_card(player_1)
    tournament.register_card(player_2)
    result_match = tournament.create_match(player_1.id_card, player_2.id_card)
    print(f"Match result: {result_match}")

    print()

    print("Tournament Leaderboard:")
    leaderboard = tournament.get_leaderboard()
    for lines in leaderboard:
        print(lines)

    print()

    print(f"Platform Report: \n {tournament.generate_tournament_report()}")

    print("=== Tournament Platform Successfully Deployed!")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
