"""Supports a round of rock, paper, scissors between a user and a computer."""
import random

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors."""
    
    valid_choices = ["rock","paper","scissors"]
    user_choice = input("Choose one: rock, paper, scissors? ")
   
    while  user_choice not in valid_choices:
        print ("Not a valid choice")
        user_choice = input("Choose one: rock, paper, scissors? ")
    return user_choice

def make_computer_choice():
    """Returns the computer's random choice of rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.

    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if choice=="rock" and opponent_choice == "scissors":
        return True
    elif choice=="scissors" and opponent_choice == "paper":
        return True
    elif choice=="paper" and opponent_choice == "rock":
        return True
    else:
        return False
    
def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    user = "user (" + str(user_score) + ")"
    computer = "computer (" + str(computer_score) + ")"
    return user + " vs. " + computer
