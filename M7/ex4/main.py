from ex4.TournamentCard import TournamentCard

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
        print(f"- Record: 0-0")
    
    print()

    try:
        Player_2 = TournamentCard("Ice wizard", "wizard_001", 1150)
    except ValueError as exc:
        print(exc)
    else:
        print(f"{Player_2.name} (ID: {Player_2.id_card})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {Player_2.rating}")
        print(f"- Record: 0-0")
    
    print()

    print("Tournament Leaderboard:")

    print("1. Fire Dragon - Rating: 1216 (1-0")


if __name__ == "__main__":
    main()