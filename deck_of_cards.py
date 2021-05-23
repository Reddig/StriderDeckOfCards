import random

DIAMOND = 'diamond'
HEART = 'heart'
SPADE = 'spade'
CLUB = 'club'
SUITS = {DIAMOND, HEART, SPADE, CLUB}
FACE_VALUES = {1: 'ace', 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 
                9:9, 10:10, 11:'jack', 12:'queen', 13:'king'}
LOCATION = {"top", "bottom", "random"}

class DeckOfCards():
    """
    This class represents a standard 52-card deck of playing cards.

    Attributes:
    deck (list): A list of DeckOfCards.Card objects.
    deck_size (int): The number of cards in the deck.
    dealt_cards (list): A list of all the cards that have been dealt.

    Methods:
    shuffle(): Randomizes the deck so that the cards will be drawn in a random order.
    deal_one_card(): Returns a DeckOfCards.Card object from the top of the deck. Removes card from deck.
    """


    def __init__(self):
        """
        Creates a deck of 52 standard playing cards in order, separated by suit.
        """
        self.deck = list()
        for suit in SUITS:
            for face_value in FACE_VALUES:
                self.deck.append(DeckOfCards.Card(suit, face_value))
        self.deck_size = 52


    def deal_one_card(self) -> DeckOfCards.Card:
        """
        Returns:
        DeckOfCards.Card: The card on top (unless no cards exist, then None)
        """
        if self.deck_size == 0:
            return None
        self.deck_size -= 1
        return self.deck.pop(self.deck_size)


    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        for card in self.deck:
            old_loc = random.randint(0,52)
            new_loc = random.randint(0,52)
            card = self.deck.pop(old_loc)
            self.deck.insert(new_loc, card)
    

    def add_card_to_deck(self, card: DeckOfCards.Card, location: str='random'):
        """
        Adds a card to the deck.

        Parameters:
        card (DeckOfCards.Card): The card to add back into the deck
        location (str): Where to add in the deck. top|bottom|random (default random)

        Raises:
        ValueError: If you try to add card that has not yet been dealt (no cheating allowed)
        """



    class Card():
        """
        This class represents a standard playing card.

        Attributes:
        suit (str): The suit of the card. diamond | heart | spade | club
        face_value (int): The value of the card (aces low) 1-13
        """
        def __init__(self, suit: str, face_value: int):
            """
            Parameters: 
            suit (str): The suit of the card. diamond | heart | spade | club
            face_value (int): The value of the card (aces low) 1-13

            Raises:
            ValueError: If suit or face_value is not in acceptable range.
            """
            if (suit.lower() not in SUITS):
                raise ValueError(f'"suit" must be a one of {SUITS}')
            self.suit = suit
            if (face_value not in FACE_VALUES):
                raise ValueError(f'"face_value" must be an integer value 1-13')
            self.face_value = face_value


        def __str__(self):
            return f'{FACE_VALUES[self.face_value]} of {self.suit}s'

        def __eq__(self, obj):
            return isinstance(DeckOfCards.Card) and obj.face_value == self.face_value