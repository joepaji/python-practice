#!/usr/bin/env python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

dict = {0: rock, 1: paper, 2: scissors}

repeat = 'y'
while repeat=='Y' or repeat == 'y':
    player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
    print("Player chose: ")
    print(dict[player_input])

    computer_input = random.randint(0,2)
    print("Computer chose: ")
    print(dict[computer_input])

    result = ""

    if player_input == computer_input: 
        result = "Draw."
    elif player_input == 0 and computer_input == 2:
        result = "You win!"
    elif computer_input == 0 and player_input == 2:
        result = "You lose!"
    elif player_input > computer_input:
        result = "You win!"
    else:
        result = "You lose!"

    print(f'\nResult: {result}')
    repeat = input("Play again? (Y/N)")