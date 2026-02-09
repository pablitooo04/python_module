from ex2.Magical import Magical
from ex2.Combatable import Combatable
from ex2.EliteCard import EliteCard
from ex0.CreatureCard  import CreatureCard

def main() -> None:
    print("=== DataDeck Ability System ===\n")


    print("EliteCard Capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):")
    arcane_warrior = EliteCard("Arcane Warrior", 7, "Epic")
    Enemy1 = CreatureCard("Enemy1", 125, "common", 25, 120)
    Enemy2 = CreatureCard("Enemy2", 125, "common", 25, 120)

    print("Combat phase:")
    attack_result = arcane_warrior.attack(Enemy1)
    defense_result = arcane_warrior.defend(15)
    print(f"Attack result: {attack_result}")
    print(f"Defense result: {defense_result}\n")

    print("Magic Phase:")
    spell_cast = arcane_warrior.cast_spell("Fireball", [Enemy1, Enemy2])
    mana_channel = arcane_warrior.channel_mana(7)
    print(f"Spell cast: {spell_cast}")
    print(f"Mana channel: {mana_channel}")
    print("Multiple interface implementation successful!")



if __name__ == "__main__":
    main()