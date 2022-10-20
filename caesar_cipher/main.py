#!/usr/bin/env python3
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    result = ""
    if direction == 'decode':
        shift *= -1
    for char in text:
        if char not in alphabet:
            result += char
        else:
            shift_index = alphabet.index(char) + shift
            if shift_index > 25:
                shift_index = shift_index%25-1
            result += alphabet[shift_index]
    print(f"The {direction}d text is '{result}'")
    return result

repeat = 'yes'
while repeat == 'yes':
    caesar(text, shift, direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if repeat == 'no':
        break
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
