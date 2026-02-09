from ex0 import Card
from random import choice


class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        try:
            index: int = self.deck.index(card_name)
        except ValueError:
            return False
        else:
            self.deck.pop(index)
            return True

    def shuffle(self) -> None:
        shuffled_deck: list = []
        for _ in range(len(self.deck)):
            card: Card = choice(self.deck)
            self.remove_card(card.name)
            self.deck.append(card)

        self.deck = shuffled_deck

    def draw_card(self) -> Card:
        if not self.deck:
            return None
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        stats = {
            'total_cards': len(self.deck),
            'creatures':
            sum(1 for card in self.deck if card.type == 'creature'),
            'spells':
            sum(1 for card in self.deck if card.type == 'spell'),
            'artifacts':
            sum(1 for card in self.deck if card.type == 'artifact'),
        }

        if self.deck:
            stats.update(
                {'avg_cost':
                 sum(card.cost for card in self.deck)/len(self.deck)})
        else:
            stats.update({'avg_cost': None})

        return stats
