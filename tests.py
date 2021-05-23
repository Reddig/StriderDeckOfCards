from deck_of_cards import DeckOfCards, HEART, DIAMOND, SPADE, CLUB, SUITS

CARDS_PER_SUIT = 13

def test_deal_all():
    deck = DeckOfCards()
    num_suits = {DIAMOND: 0, HEART: 0, SPADE: 0, CLUB:0}
    num_face_values = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}

    for _ in range(0, 52):
        card = deck.deal_one_card()
        num_suits[card.suit] += 1
        num_face_values[card.face_value] += 1

    for suit in num_suits:
        assert(suit in SUITS)   # ensure we didn't get some unexpected non-suit suit
        assert(num_suits[suit] == CARDS_PER_SUIT)