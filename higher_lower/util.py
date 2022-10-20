from art import logo, vs
from game_data import data
from os import system
#from main import celebrity1, celebrity2, score
import random

score = 0
highscore = 0

def init_game():
    print(logo)

def get_hilo(celebrity1, celebrity2):
    """Shows celebrity info and prompts user for higher or lower guess"""
    print(f"{celebrity1['name']}, {celebrity1['description']}, from {celebrity1['country']}")
    print(vs)
    print(f"{celebrity2['name']}, {celebrity2['description']}, from {celebrity2['country']}")
    
    print(f"{celebrity1['name']} has {celebrity1['follower_count']} followers.")
    print(f"How many followers do you think {celebrity2['name']} has?: ")
    print(f"1: Higher")
    print(f"2: Lower")
    hilo = int(input("Enter 1 or 2 to select your option: "))
    return hilo

def get_new_celeb(existing_celeb):
    """Gets a new celebrity at random that isn't a duplicate"""
    new_celeb = random.choice(data)
    while new_celeb == existing_celeb:
        new_celeb = random.choice(data)
    return new_celeb

def check_answer(hilo, celebrity1, celebrity2):
    """Checks if given answer is correct. Returns true if correct."""    
    global highscore
    higher = celebrity2['follower_count']>celebrity1['follower_count']   
    
    if hilo == 1 and higher:
        add_score()
        if score > highscore:
            highscore = score
        return True
    elif hilo == 1 and not higher:
        return False
    elif hilo == 2 and higher:
        return False
    else:
        add_score()
        if score > highscore:
            highscore = score
        return True

def print_game_over():
    """Called when wrong guess is made. Prints game over and clears score."""
    system('clear')
    print(logo)
    print(f"Sorry, that's not correct. Final score: {score}   High score: {highscore}")
    reset_score()

def clear_print_logo():
    """Clears screen and prints logo"""
    system('clear')
    print(logo)

def add_score():
    global score
    score += 1

def reset_score():
    global score
    score = 0

def game():
    """This method executes the game code"""
    global highscore
    init_game()
    correct_answer = True
    celebrity1, celebrity2 = random.sample(data, 2)
    hilo = get_hilo(celebrity1, celebrity2)
    correct_answer = check_answer(hilo, celebrity1, celebrity2)
    while correct_answer:
        celebrity1 = celebrity2
        celebrity2 = get_new_celeb(celebrity1)
        clear_print_logo()
        print(f"You are right! Current score: {score}   High score: {highscore}")
        hilo = get_hilo(celebrity1, celebrity2)
        correct_answer = check_answer(hilo, celebrity1, celebrity2)
    if not correct_answer:
        print_game_over()