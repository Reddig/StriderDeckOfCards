from deck_of_cards import DeckOfCards, HEART, DIAMOND, SPADE, CLUB, SUITS

CARDS_PER_SUIT = 13

def test_deal_all():
    """
    Check all cards in a standard deck are as expected
    """
    deck = DeckOfCards()
    num_suits = {DIAMOND: 0, HEART: 0, SPADE: 0, CLUB:0}
    num_face_values = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}

    for _ in range(0, 52):
        card = deck.deal_one_card()
        num_suits[card.suit] += 1
        num_face_values[card.face_value] += 1

    assert(deck.deck_size == 0)

    for suit in num_suits:
        assert(suit in SUITS)   # ensure we didn't get some unexpected non-suit suit
        assert(num_suits[suit] == CARDS_PER_SUIT)
    
    for key, value in num_face_values.items():
        assert(value == 4)  # ensure 4 of each value
        assert (key > 0 and key < 14)   # ensure 1-13


def test_shuffle():
    """
    Check that all cards intact after shuffling
    """
    deck = DeckOfCards()
    deck.shuffle()

    num_suits = {DIAMOND: 0, HEART: 0, SPADE: 0, CLUB:0}
    num_face_values = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}

    for _ in range(0, 52):
        card = deck.deal_one_card()
        num_suits[card.suit] += 1
        num_face_values[card.face_value] += 1

    for suit in num_suits:
        assert(suit in SUITS)   # ensure we didn't get some unexpected non-suit suit
        assert(num_suits[suit] == CARDS_PER_SUIT)
    
    for key, value in num_face_values.items():
        assert(value == 4)  # ensure 4 of each value
        assert (key > 0 and key < 14)   # ensure 1-13


def test_add_card():
    """
    Check you can insert a dealt card, and you cannot insert an undealt card.
    """
    deck = DeckOfCards()
    card = deck.deal_one_card()
    assert(card not in deck.deck)
    deck.add_card_to_deck(card)
    assert(card in deck.deck)

    expected_err = None
    try:
        deck.add_card_to_deck(card)
    except ValueError as e:
        expected_err = e
    assert(expected_err is not None)

def test_add_card_top():
    """
    Check if we pull a card from the top and put it back on top, that it stays on top.
    """
    deck = DeckOfCards()
    old_top_card = deck.deal_one_card()
    deck.add_card_to_deck(old_top_card, 'top')
    new_top_card = deck.deal_one_card()

    assert(new_top_card == old_top_card)

def test_add_card_bottom():
    """
    Check if we pull a card from the top and put it on the bottom, that is stays on bottom.
    """
    deck = DeckOfCards()
    old_top_card = deck.deal_one_card()
    deck.add_card_to_deck(old_top_card, 'bottom')
    for _ in range(deck.deck_size - 1):
        card = deck.deal_one_card()
        assert(card != old_top_card)
    new_bottom_card = deck.deal_one_card()
    assert(old_top_card == new_bottom_card)

def test_shuffle_after_deal():
    """
    Check shuffle works after dealing a card.
    """
    deck = DeckOfCards()
    deck.deal_one_card()

    unshuffled_deck = deck.deck.copy()
    deck.shuffle()
    assert(deck.deck != unshuffled_deck)