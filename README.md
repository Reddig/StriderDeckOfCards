## Deck of Cards
This library provides an extensive Deck of Cards functionality for you and your organization.

### Creating a deck of cards
Simply instantiate a DeckOfCards object.
```python
deck_of_cards = DeckOfCards()
```

### Shuffling
```python
deck_of_cards = DeckOfCards  # create a deck of cards
deck_of_cards.shuffle() # shuffle it! - your cards are now in a random order 
```

### Dealing
```python
deck_of_cards = DeckOfCards  # create a deck of cards
card = deck_of_cards.deal_one_card()
print(card) # ace of spades
```

### Replacing Cards
#### Shuffling Card In
```python
deck_of_cards = DeckOfCards  # create a deck of cards
card = deck_of_cards.deal_one_card()
deck_of_cards.add_card_to_deck(card)
```
#### Add Card to Top/Bottom
```python
deck_of_cards = DeckOfCards  # create a deck of cards
card = deck_of_cards.deal_one_card()
location = 'top' | 'bottom' # add card in at top or bottom of deck
deck_of_cards.add_card_to_deck(card, location)
```

#### Usage
See examples for a basic blackjack game made using this library.