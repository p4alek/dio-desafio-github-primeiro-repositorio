from random import shuffle

total = 500
minimum_bet = 1
bet = 0
bust = False
blackjack = False
deck = []
player_cards = []
dealer_cards = []


def welcome():
    print('Welcome to Blackjack!\n')


def want_to_play():
    global total

    print(f'You are starting with ${total}. ', end="")
    while True:
        start = input('Would you like to play a hand? (yes/no) ').lower()
        if start == 'yes' or start == 'no':
            break
        else:
            print('Invalid option.')

    return start == 'yes'


def finish_game():
    global total

    print(f'\nHave a good day. You left with ${total}.')


def create_deck():
    suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
    cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(suit + card)

    return deck


def shuffle_cards():
    global deck, player_cards, dealer_cards

    player_cards = dealer_cards = []
    deck = create_deck()
    shuffle(deck)


def bet_game():
    global total, minimum_bet, bet

    while True:
        try:
            bet = float(input('Place your bet: '))
            if bet < minimum_bet:
                print(f'The minimum bet is ${minimum_bet}.')
            elif bet > total:
                print(f'You do not have sufficient funds.')
            else:
                total -= bet
                break

        except:
            print('Invalid bet.')

    shuffle_cards()


def deal_cards():
    global deck, player_cards, dealer_cards, blackjack, total

    player_cards = [deck.pop(), deck.pop()]
    dealer_cards = [deck.pop(), deck.pop()]

    print(f'You are dealt: {player_cards[0]}, {player_cards[1]}')
    print(f'The dealer is dealt: {dealer_cards[0]}, Unknown')

    if count_cards(player_cards) == 21 and count_cards(dealer_cards) != 21:
        print(f'Blackjack! You win ${bet * 1.5} :)')
        blackjack = True
        total += bet * 2.5

    if count_cards(player_cards) == 21 and count_cards(dealer_cards) == 21:
        print('You tie. Your bet has been returned.')
        blackjack = True
        total += bet


def player():
    global deck, player_cards, bet, bust

    while True:
        hit_stay = input('Would you like to hit or stay? (hit/stay) ')
        if hit_stay != 'hit' and hit_stay != 'stay':
            print('That is not a valid option.')
        else:
            if hit_stay == 'hit':
                card = deck.pop()
                player_cards.append(card)
                if count_cards(player_cards) > 21:
                    print(f'Your hand value is over 21 and you lose ${bet} :(')
                    bust = True
                    break
                else:
                    print(f'You are dealt: {card}')
                    print(f'You now have: {player_cards}')
            else:
                break


def dealer():
    global deck, dealer_cards, bust, bet

    while count_cards(dealer_cards) < 17:
        card = deck.pop()
        dealer_cards.append(card)
        print(f'The dealer hits and is dealt: {card}')
        print(f'The dealer has: {dealer_cards}')
        if count_cards(dealer_cards) > 21:
            print(f'The dealer busts, you win ${bet} :)')
            bust = True
            break

    print('The dealer stays.')


def game():
    global player_cards, dealer_cards, bet, total

    if count_cards(player_cards) == count_cards(dealer_cards):
        print('You tie. Your bet has been returned.')
        total += bet
    elif count_cards(player_cards) > count_cards(dealer_cards):
        print(f'You win ${bet}!')
        total += bet * 2
    else:
        print(f'The dealer wins, you lose ${bet} :(')


def count_cards(cards):
    d = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10}
    total = 0
    filter = []
    for card in cards:
        filter.append(card[1:])
    if len(cards) == 2 and filter[0] == 'A' and filter[1] == 'A':
        return 20
    elif 'A' not in filter:
        for value in filter:
            total += d[value]
        return total
    elif 'A' in filter:
        for value in filter:
            total += d.get(value, 0)
        if total <= 10:
            total += 11
        else:
            total += 1
        return total


def main():
    global total, bust
    welcome()
    while total > 0 and want_to_play():
        bet_game()
        deal_cards()
        if not blackjack:
            player()
            if not bust:
                dealer()
            if not bust:
                game()

    if total == 0:
        print("\nYou've ran out of money. Please restart this program to try again. Goodbye.")
    finish_game()


if __name__ == '__main__':
    main()