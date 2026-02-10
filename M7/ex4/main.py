from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")
    try:
        Player_1 = TournamentCard("Fire Dragon", "dragon_001", 1200)
    except ValueError as exc:
        print(exc)
    else:
        print(f"{Player_1.name} (ID: {Player_1.id_card})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {Player_1.rating}")
        print("- Record: 0-0")

    print()

    try:
        Player_2 = TournamentCard("Ice wizard", "wizard_001", 1150)
    except ValueError as exc:
        print(exc)
    else:
        print(f"{Player_2.name} (ID: {Player_2.id_card})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {Player_2.rating}")
        print("- Record: 0-0")

    print()
    print("Creating tournament match...")
    tournament = TournamentPlatform()
    tournament.register_card(Player_1)
    tournament.register_card(Player_2)
    result_match = tournament.create_match(Player_1.id_card, Player_2.id_card)
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
