#!/usr/bin/env python3
import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv('nato_phonetic_alphabet.csv')
dict = {row.letter:row.code for (index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")
phonetic_code = [dict[char.upper()] for char in word]
print(phonetic_code)
