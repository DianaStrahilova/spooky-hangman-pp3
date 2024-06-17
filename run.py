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
    while True:
        typewriter("Do you want to rea")



