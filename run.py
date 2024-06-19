import random
import sys
import os
import string
from time import sleep
from words import words
from ascii_art import print_rules
from ascii_art import logo
from ascii_art import game_over
from ascii_art import winner
from ascii_art import bye
from hangman_stages import hangman_stages


def typewriter(text):
    """
    Print statements with typewriter effect.
    """
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def clear_terminal():
    """ 
    Clears the terminal for better user experience.
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
            print_rules()
            print("\n")
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
    user_name = input("Enter your name if you dare: \n").strip()
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
            print("\nYou already guessed the letter", user_guess, ". Guess another one.")
        else:
            clear_terminal()
            print("Not a valid letter")
    
    if lives == 0:
        print(hangman_stages[lives])
        typewriter("Too bad... the word was: ")
        typewriter(secret_word)
        print("\n")
        game_over()
        play_again()
    else:
        typewriter("Awesome! You guessed the word: ")
        typewriter(secret_word)
        print('!')
        winner()
        play_again()


def play_again():
    user_choice = input("Dare to play again? (Y/N)\n").strip().upper()
    if user_choice == "N":
        print("\nToo bad... May the HORROR stay with you! :(")
        bye()
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
    logo()
    typewriter("Welcome! Dare to enter the chilling world of SPOOKY HANGMAN?\n")
    print("\n")
    rules()
    user_name()
    play()

"""
if __name__ == "main":
    main()
"""
main()












