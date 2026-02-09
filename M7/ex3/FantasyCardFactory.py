from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity, Card
from ex1.Deck import Deck
import random


class FantasyCardFactory(CardFactory):
    cards = {'artifacts': [
            ("Mana Crystal", 2, Rarity.UNCOMMON.value, 5, "Permanent: +1 mana"),
            ("Magic Ring", 3, Rarity.RARE.value, 10, "Permanent: +2 mana"), 
            ("Ancient Staff", 4, Rarity.EPIC.value, 12, "Permanent: +3 mana")
        ],  
            'creatures': [
            ("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5), 
            ("Goblin Warrior", 2, Rarity.COMMON.value, 3, 2)
        ],
            'spells': [
            ("Fireball", 4, Rarity.RARE.value, "damage"), 
            ("Lightning Bolt", 3, Rarity.COMMON.value, "damage"), 
            ("Ice Shard", 2, Rarity.UNCOMMON.value, "damage")
        ]
    }
    
    def create_creature(self, name_or_power: str=None) -> Card:
        creatures = FantasyCardFactory.cards["creatures"]
        creatures_name = [c[0].lower() for c in creatures]
        if name_or_power is None:
            return CreatureCard(*(random.choice(creatures)))
        elif name_or_power.lower() in creatures_name:
            return CreatureCard(*(creatures[creatures_name.index(name_or_power.lower())]))
        else:
            raise ValueError("Error: Invalid Creature!")
        

    def create_spell(self, name_or_power: str=None) -> Card:
        spells = FantasyCardFactory.cards["spells"]
        spells_name = [s[0].lower() for s in spells]
        if name_or_power is None:
            return SpellCard(*(random.choice(spells)))
        elif name_or_power.lower() in spells_name:
            return SpellCard(*(spells[spells_name.index(name_or_power.lower())]))
        else:
            raise ValueError("Error: Invalid Spell!")

    def create_artifact(self, name_or_power: str=None) -> Card:
        artifacts = FantasyCardFactory.cards["artifacts"]
        artifacts_name = [n[0].lower() for n in artifacts]
        if name_or_power is None:
            return ArtifactCard(*(random.choice(artifacts)))
        elif name_or_power.lower() in artifacts_name:
            return ArtifactCard(*(artifacts[artifacts_name.index(name_or_power.lower())]))
        else:
            raise ValueError("Error: Invalid Artifact!")


    def create_themed_deck(self, size: int) -> dict:
        if isinstance(size, int) and size > 0:
            hand = {}
            deck = []
            for i in range(size):
                n = random.randint(0, 2)
                if n == 0:
                    created_item = self.create_creature()
                elif n == 1:
                    created_item = self.create_spell()
                else:
                    created_item = self.create_artifact()
                deck.append(created_item)
                if not created_item.name in hand:
                    hand[created_item.name] = 1
                else:
                    hand[created_item.name] += 1
        else:
            raise ValueError("Error: Invalid size!")
        return {"hand": hand, 'deck': deck}

    def get_supported_types(self) -> dict:
        return FantasyCardFactory.cards
