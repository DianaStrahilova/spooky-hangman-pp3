
# Import section

# pyfiglet takes ASCII text and renders it in ASCII art fonts.
import pyfiglet 
#figlet_format method convert ASCII text into ASCII art fonts.
from pyfiglet import figlet_format 
# termcolor to add colors to the banners.
import termcolor
from termcolor import colored


# Print rules
def print_rules():
    print("============================================================================")
    print("|| ---------------------------------------------------------------------  ||")
    print("||                         ==========================                     ||")
    print("||                                 GAME RULES                             ||")
    print("||                         ==========================                     ||")                                                                                   
    print("|| HOW TO PLAY:                                                           ||")
    print("|| 1. Objective: Guess the creepy hidden word, one letter at a time.      ||")
    print("|| 2. Lives: You have a limited number of incorrect guesses before        ||")
    print("|| the spirit is lost.                                                    ||")
    print("|| 3. Clues: Use the eerie underscores _ _ _ _ to see how many            ||")
    print("|| letters are in the word.                                               ||")
    print("|| 4. Guessing: Each correct letter guessed will reveal its position      ||")
    print("|| in the word                                                            ||")
    print("|| 5. Win: Complete the word before running out of guesses to win the game||")
    print("|| 6. Lose: Run out of guesses and the spirit faces a spooky end!         ||")
    print("||                                                                        ||")
    print("||    GOOD LUCK!                                                          ||")
    print("||  ----------------------------------------------------------------------||")
    print("============================================================================")


# Prints logo
def logo():
    logo = figlet_format("SPOOKY HANGMAN")
    colored_logo = colored(logo, 'yellow')
    print(colored_logo)


# Prints game over
def game_over():
    game_over = figlet_format("GAME OVER")
    colored_game_over = colored(game_over, 'red')
    print(colored_game_over)


# Prints you win
def winner():
    you_win = figlet_format("YOU WIN !")
    colored_win = colored(you_win, 'green') 
    print(colored_win)


# Prints bye bye
def bye():
    bye = pyfiglet.figlet_format("BYE BYE")
    colored_bye = colored(bye, 'blue')
    print(colored_bye)



