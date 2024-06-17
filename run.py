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
    user_name = input("Enter your name if you dare:\n").strip()
    if user_name == "":
        user_name = "Joker"
    clear_terminal()
    typewriter((f"Howdy, {user_name}. Time to play :O!\n"))
    print()


def get_word():
    """
    Function to pick a random word from the word list
    """
    word = random.choice(words)
    return word.upper()


def play():
    """
    Function to start and play the game.
    """
    secret_word = get_word()
    secret_letters = set(secret_word)
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set()
    
    lives = 6

    while len(secret_letters) > 0 and lives > 0:
        print("You have", lives, "lives left\n")
        print("Guessed letters: ", ' '.join(guessed_letters))

        word_list = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print(hangman_stages[lives])
        print("Current word: ", ' '.join(word_list))
        print()

        user_guess = input("Guess a letter:\n").upper()
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in secret_letters:
                secret_letters.remove(user_guess)
                print("")
                clear_terminal()
            else:
                lives = lives - 1
                print("\n Letter: ", user_guess, "is not in the word.")
                clear_terminal()
        elif user_guess in guessed_letters:
            clear_terminal()
            print("\nYou already guessed the letter", user_guess, ". Guess another one")
        else:
            clear_terminal()
            print("Not a valid letter")
    
    if lives == 0:
        print(hangman_stages[lives])
        typewriter("The guy is dead ... the word was: ")
        typewriter(secret_word)
        print(GAME_OVER)
        play_again()
    else:
        typewriter("Awesome! You guessed the word: ")
        typewriter(secret_word)
        print('!')
        print(WINNER)
        play_again()


def play_again():
    user_choice = input("Dare to play again? (Y/N)\n").strip().upper()
    if user_choice == "N":
        print("\nToo bad... May the HORROR stay with you! :(")
        print(BYE)
    elif user_choice == "Y":
        print("Awesome! Let's play again!")
        clear_terminal()
        play()
    else:
        print("Invalid choice... please enter 'y' or 'n'.")
        play_again()

def main():
    print("SPOOKY HANGMAN")
    print("By Diana Strahilova")
    print(LOGO)
    typewriter("Welcome! Dare to enter the chilling world of SPOOKY HANGMAN?\n")
    print("\n")
    rules()
    user_name()
    play()
    play_again()

main()
    










