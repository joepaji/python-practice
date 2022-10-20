#!/usr/bin/env python3
from os import system
import art

# header
print(art.logo)
print("Welcome to the secret auction program")

highest_bidder = ""
other_bidders = "yes"
bidders = {}

while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid
    highest_bid = 0
    for n in bidders:
        if int(bidders[n])>highest_bid:
            highest_bid = int(bidders[n])
            highest_bidder = n
    other_bidders = input("Are there any other bidders?: ").lower()
    if other_bidders == "yes":
        system('clear')

system('clear')
print(f"The winner is {highest_bidder} with a bid of ${bidders[highest_bidder]}")