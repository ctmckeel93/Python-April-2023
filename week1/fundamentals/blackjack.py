import random
from colorama import Fore, Style 

card_values = [11,10,10,10,10,9,8,7,6,5,4,3,2]

full_deck = card_values * 4 # we can also do this instead of creating the nested loop below
print("Full deck:", full_deck)


def play_game():
    deck = make_deck()
    random.shuffle(deck)
    players = deal(deck)
    display_totals(players,deck)


def make_deck():
    cards = []

    # nested loops will run as many times as the product of the number of loops. 4 x 13 = 52
    # This loop will run 52 times
    for i in range(4): # starts at 0 and loops 4 times
        for j in range(13): # starts at 0 and loops 13 times
            cards.append(card_values[j])
    return cards

def deal(deck):
    player_hand = []
    dealer_hand = []
    player_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    return  dealer_hand,player_hand

def check_cards(hand,deck):
    while True:
        if sum(hand) == 21:
            print("Blackjack!!!!!")
            return sum(hand)
        elif sum(hand) < 18:
            hand.append(deck.pop())
            if sum(hand) > 21:
                print("Oops you broke")
                return sum(hand)
        else: 
            print("Good enough")
            return sum(hand)
        
def display_totals(players,deck):
    print("Dealer".center(20, "="))
    dealer_total = check_cards(players[0],deck)
    print("Dealer:", dealer_total)
    print("Player".center(20, "="))
    player_total = check_cards(players[1],deck)
    print("Player:", player_total)
    check_for_winner(dealer_total, player_total)

def check_for_winner(dealer_total, player_total):
    if dealer_total == 21:
        return resolve()
    elif player_total > dealer_total and player_total <= 21:
        return resolve("Player", Fore.GREEN)
    elif dealer_total > 21:
        return resolve("Player", Fore.GREEN) 
    else: 
        return resolve()

def resolve(winner="Dealer" ,color=Fore.RED):
    print(color + winner, "wins")
    print(Style.RESET_ALL)
    return winner

play_game() # This starts the game | see if you can follow the flow of the code. 