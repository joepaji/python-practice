#!/usr/bin/env python3

import util
import art

print(art.logo)

play = input("Would you like to play a game of BlackJack?(y/n): ").lower()
cash = 0
if play =='y':
    cash = int(input("Enter the total amount of cash: $"))
player_cash = cash

while play == 'y' and player_cash>0:
    pot = 200
    player_cash -= 100    
    player_hand = []
    dealer_hand = []
    util.deal_cards(player_hand, 2)
    util.deal_cards(dealer_hand, 2)

    player_sum = sum(player_hand)
    dealer_sum = sum(dealer_hand)

    if player_sum == 22:
        player_hand[0] = 1
        player_sum = sum(player_hand)

    if dealer_sum == 22:
        dealer_hand[0] = 1
        dealer_sum = sum(dealer_hand)

    print(f"Cash: ${player_cash}   Pot: ${pot}")
    print(f"Your cards: {player_hand}   Sum: {player_sum}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    if player_sum == 21:
        if dealer_sum == 21:
            print("Draw!")
            player_cash += int(pot/2)
        else:
            player_cash += pot
            print(f"Cash: ${player_cash}   Pot: ${pot}")
            print("You Win!\n")
            play = input("Would you like to play a game of BlackJack?(y/n): ").lower()
            continue
    
    if dealer_sum == 21:
        pot = 0
        util.display_status(player_hand, dealer_hand, player_cash, pot)
        print("Dealer wins!\n")

    player_cash, pot = util.player_turn(player_hand, dealer_hand, player_cash, pot)
    player_sum = sum(player_hand)

    if player_sum == 21:
        player_cash += pot
        pot = 0
        print(f"Cash: ${player_cash}   Pot: ${pot}")
        print("Blackjack! You win!\n")
    elif player_sum > 21:
        pot = 0
        util.display_status(player_hand, dealer_hand, player_cash, pot)
        print("Dealer wins!\n")
        
    else:
        util.dealer_turn(player_hand, dealer_hand)
        dealer_sum = sum(dealer_hand)

        if dealer_sum == 21:
            pot = 0
            util.display_status(player_hand, dealer_hand, player_cash, pot)
            print("Blackjack! Dealer wins!\n")
        elif dealer_sum > 21:
            player_cash += pot
            pot = 0
            util.display_status(player_hand, dealer_hand, player_cash, pot)
            print("You win!\n")
        elif dealer_sum < player_sum:
            player_cash += pot
            pot = 0
            util.display_status(player_hand, dealer_hand, player_cash, pot)
            print("You win!\n")
        elif dealer_sum == player_sum:
            player_cash += int(pot/2)
            pot = 0
            util.display_status(player_hand, dealer_hand, player_cash, pot)
            print("Draw!\n")
        else:
            pot = 0
            util.display_status(player_hand, dealer_hand, player_cash, pot)
            print("Dealer wins!\n")

    play = input("Would you like to play a game of BlackJack?(y/n): ").lower()