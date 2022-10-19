#!/usr/bin/env python3

#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def insert_at(string, char, index):
    return string[:index] + char + string[index:]

count = {'letters': nr_letters, 'numbers': nr_numbers, 'symbols': nr_symbols} 
characters = [letters, numbers, symbols]
password = ""

length = nr_letters + nr_numbers + nr_symbols

while count['letters'] != 0 or count['numbers'] != 0 or count['symbols'] != 0:
    char_pick = random.randint(0, 2)
    if char_pick == 0:
        if count['letters'] == 0:
            continue
        else:
            password += letters[random.randint(0,len(letters)-1)]
            count['letters'] -= 1

    elif char_pick == 1:
        if count['numbers'] == 0:
            continue
        else:
            password += numbers[random.randint(0,len(numbers)-1)]
            count['numbers'] -= 1
    
    else:
        if count['symbols'] == 0:
            continue
        else:
            password += symbols[random.randint(0,len(symbols)-1)]
            count['symbols'] -= 1

print(password)