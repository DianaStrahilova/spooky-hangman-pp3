import random
import sys
from time import sleep
from words import words
from textart import RULES
from textart import LOGO
from textart import GAME_OVER
from textart import WINNER
from textart import BYE
from hangman_stages import hangman_stages
import os
import string

def typewriter(text):
    """
    Print statements with typewriter effect.
    """
    for char in text:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

def clear_terminal():
    """ 
    Clears the terminal for better user experience
    """
    os.system("cls" if os.name == "nt" else "clear")


def rules():
    """
    Function to display the game rules if user chooses to.
    """
    while True:
        typewriter("Do you want to read the game rules? (Y/N)")
        answer = input().upper().strip()
        if answer == "Y":
            print(RULES)
            return True
        elif answer == "N":
            print("Let's play then!")
            break
        else:
            print("Invalid character. Please enter 'Y' or 'N'.")

def user_name():
    """
    Function prompting the user to input their name.
    """
    user_name = input("Enter your name if you dare: ").strip()
    if user_name == "":
        user_name = "Joker"
        clear_terminal()
        typewriter((f"Howdy, {user_name}. Time to play :O!\n"))
        print()






