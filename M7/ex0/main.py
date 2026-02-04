from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    dragon_card = CreatureCard("Fire Dragon", 5, "Legendary", 5, 5)
    goblin_card = CreatureCard("Goblin Warrior", 5, "Legendary", 7, 10)

    mana = 6
    print("CreatureCard Info:")
    print(f"{dragon_card.get_card_info()}\n")

    print(f"Playing {dragon_card.name} with {mana} mana available:")
    print(f"Playable: {dragon_card.is_playable(mana)}")
    game_state = {"active": True, "mana": mana}
    print(f"Play result: {dragon_card.play(game_state)}\n")

    print(f"{dragon_card.name} attacks {goblin_card.name}:")
    print(f"Attack result: {dragon_card.attack_target(goblin_card)}\n")

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon_card.is_playable(3)}\n")

    print("Abstract pattern successfully demonstrated!")
