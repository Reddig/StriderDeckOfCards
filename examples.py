from deck_of_cards import DeckOfCards, Card

def blackjack():
    deck = DeckOfCards()
    deck.shuffle()

    player_cards = [deck.deal_one_card(), deck.deal_one_card()]

    dealer_cards = [deck.deal_one_card(), deck.deal_one_card()]
    print(f'You have been dealt {player_cards[0]} and {player_cards[1]}')
    print(f'Dealer is showing {dealer_cards[0]}')
    player_total_ace_low, player_total_ace_high = sum_cards(player_cards)
    dealer_total_ace_low = dealer_total_ace_high = sum_cards(dealer_cards)

    # player's turn, can hit or stand
    choice = 'h'
    while choice == 'h':
        if player_total_ace_high == 21 or player_total_ace_low == 21:
            print('You have 21, auto-standing.')
            break

        choice = input('Hit (h) or stand (s)? ')
        if choice == 'h':
            card = deck.deal_one_card()
            print(f'You draw {card}')
            player_cards.append(card)
            player_total_ace_low, player_total_ace_high = sum_cards(player_cards)
            if player_total_ace_high != player_total_ace_low:
                print(f'Your total is {player_total_ace_low}/{player_total_ace_high}')
            else:
                print(f'Your total is {player_total_ace_low}')
            
            if player_total_ace_high > 21 and player_total_ace_low > 21:
                print("You bust!")
                return
    print(f'Dealer reveals {dealer_cards[1]}') # dealer flips over face down card

    dealer_total_ace_low, dealer_total_ace_high = sum_cards(dealer_cards)
    # dealer must stand on a 17 or higher, hit on 16 or lower
    while dealer_total_ace_low < 17 and dealer_total_ace_high < 17:
        card = deck.deal_one_card()
        print(f'Dealer draws {card}')
        dealer_cards.append(card)
        dealer_total_ace_low, dealer_total_ace_high = sum_cards(dealer_cards)
    if dealer_total_ace_high > 21 and dealer_total_ace_low > 21:
            print("Dealer busts, you win!")
            return    
    player_total = player_total_ace_low
    if player_total_ace_high <= 21:
        player_total = player_total_ace_high
    
    dealer_total = dealer_total_ace_low
    if dealer_total_ace_high <= 21:
        dealer_total = dealer_total_ace_high
    
    print(f'Dealer finishes with {dealer_total}, you finish with {player_total}')

    if dealer_total >= player_total:
        print('You lose!')
    else:
        print('You win!')


def sum_cards(cards):
    total_ace_high = 0
    total_ace_low = 0
    for card in cards:
        if card.face_value > 1 and card.face_value < 10:
            total_ace_high += card.face_value
            total_ace_low += card.face_value
        elif card.face_value > 9: # face cards worth 10
            total_ace_high += 10
            total_ace_low += 10
        else:
            total_ace_high += 11
            total_ace_low += 1
    return (total_ace_low, total_ace_high)

    
play_again = True
while play_again:
    blackjack()
    if input('Want to play again? (y/n) ') == 'n':
        break
    print('--------------------------------------------------------')
    print('|                      NEW ROUND                       |')
    print('--------------------------------------------------------')
              
