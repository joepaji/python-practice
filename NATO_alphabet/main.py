#!/usr/bin/env python3
import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv('nato_phonetic_alphabet.csv')
dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ")
    try:
        phonetic_code = [dict[char.upper()] for char in word]
    except KeyError: 
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code)

generate_phonetic()