import random
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards(hand, n):
    if n>2:
        print("Error, can't deal more than 2 cards.")
        exit(1)
    for i in range(n):
        hand.append(cards[random.randint(0,len(cards)-1)])

def player_turn(phand, dhand, cash, pot):
    action = input("Type 'y' to Hit, type 'n' to Stand, type 'x' to 2x the bet and hit: ").lower()
    player_sum = sum(phand)
    while action == 'y' or action == 'x' and player_sum < 21:
        if action == 'x':
            cash -= pot
            pot *= 2
        deal_cards(phand, 1)
        if phand[-1] == 11 and sum(phand)>21:
            phand[-1] = 1
        player_sum = sum(phand)
        print(f"\nCash: ${cash}   Pot: ${pot}")
        print(f"Your cards: {phand}   Sum: {player_sum}")
        print(f"Dealer's first card: {dhand[0]}")
        if player_sum >= 21:
            break
        action = input("Type 'y' to Hit, type 'n' to Stand, type 'x' to 2x the bet and hit: ").lower()
    return cash, pot
    
def dealer_turn(phand, dhand):
    risk_threshold = random.choice([6, 5, 4, 3, 2, 1])
    dealer_sum = sum(dhand)
    while 21-dealer_sum>risk_threshold and dealer_sum < 21 and dealer_sum < sum(phand):
        deal_cards(dhand, 1)
        if dhand[-1] == 11 and sum(dhand)>21:
            dhand[-1] = 1
        dealer_sum = sum(dhand)
        print(f"\nYour cards: {phand}   Sum: {sum(phand)}")
        print(f"Dealer's cards: {dhand}   Sum: {dealer_sum}")
        sleep(3)

def display_status(phand, dhand, player_cash, pot):
    print(f"\nCash: ${player_cash}   Pot: ${pot}")
    print(f"Your cards: {phand}   Sum: {sum(phand)}")
    print(f"Dealer's cards: {dhand}   Sum: {sum(dhand)}")