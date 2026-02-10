
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


def main() -> None:
    """
    Main function to demonstrate the Deck class and its interaction.
    """
    print("\n=== DataDeck Deck Builder ===\n")

    print("Building deck with different card types...")
    dragon_card = CreatureCard(
        "Fire Dragon", 5, Rarity.LEGENDARY.value, 5, 5)
    lightning_bolt_card = SpellCard(
        "Lightning Bolt", 3, Rarity.COMMON.value, "damage")
    mana_crystal_card = ArtifactCard(
        "Mana Crystal", 2, Rarity.COMMON.value, 5,
        "Permanent: +1 mana per turn")
    deck_1 = Deck()
    deck_1.add_card(dragon_card)
    deck_1.add_card(lightning_bolt_card)
    deck_1.add_card(mana_crystal_card)

    print(deck_1.get_deck_stats())

    print()
    print("Drawing and playing cards:")

    for _ in range(3):
        print()
        drawed_card = deck_1.draw_card()
        print(f"Drew: {drawed_card.name} ({drawed_card.type})")
        play_result = drawed_card.play({"active": True, "mana": 5})
        print(play_result)

    print("\nPolymorphism in action: Same interface, ", end="")
    print("different card behaviors!")


if __name__ == "__main__":
    main()
