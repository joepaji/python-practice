#!/usr/bin/env python3

from util import game


play_again = 'y'
while play_again == 'y':
    game()
    play_again = input("Would you like to go again? (Y/N): ").lower()


