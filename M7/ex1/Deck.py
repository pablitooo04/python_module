from ex0.Card import Card
from random import choice


class Deck:
    """A class representing a deck of cards in a card game."""
    def __init__(self) -> None:
        """Initializes an empty deck of cards."""
        self.deck = []

    def add_card(self, card: Card) -> None:
        """Adds a card to the deck.
        Args:
            card (Card): The card to be added to the deck.
        """
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """Removes a card from the deck by its name.
        Args:
            card_name (str): The name of the card to be removed.
        Returns:
            bool: True if the card was successfully removed, False else"""
        try:
            index: int = [card.name for card in self.deck].index(card_name)
        except ValueError:
            return False
        else:
            self.deck.pop(index)
            return True

    def shuffle(self) -> None:
        """
        Shuffles the deck of cards randomly.
        """
        shuffled_deck: list = []
        for _ in range(len(self.deck)):
            card: Card = choice(self.deck)
            self.remove_card(card.name)
            shuffled_deck.append(card)

        self.deck = shuffled_deck

    def draw_card(self) -> Card:
        """
        Draws a card from the top of the deck.
        Returns:
            Card: The card drawn from the top of the deck, or
            None if the deck is empty.
        """
        if not self.deck:
            raise ValueError("Error: Deck is empty!")
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        """
        Returns a dictionary containing statistics about the deck.
        """
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
