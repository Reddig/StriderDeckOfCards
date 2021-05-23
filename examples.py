from deck_of_cards import DeckOfCards

deck = DeckOfCards()

#   Simply print out all cards as they exist at deck creation
#   Something to note is that the suits are in a random order
#   as sets are unordered. I didn't see any particular reason
#   to preserve a specific order for the suits, so I think that this is okay.
# for _ in range(52):
#     print(deck.deal_one_card())


#   Shuffle cards, then print out in the new shuffled order.
deck.shuffle()
for _ in range(52):
    print(deck.deal_one_card())