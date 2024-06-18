import pyfiglet
from pyfiglet import figlet_format
import termcolor
from termcolor import colored

def print_rules():
       print("===========================================================================")
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


       


def logo():
       logo = pyfiglet.figlet_format("SPOOKY HANGMAN")
       colored_logo = colored(logo, 'yellow')
       print(colored_logo)


def game_over():
    game_over = pyfiglet.figlet_format("GAME OVER")
    colored_game_over = colored(game_over, 'red')
    print(colored_game_over)


def winner():
       you_win = pyfiglet.figlet_format("YOU WIN !")
       colored_win = colored(you_win, 'green') 
       print(colored_win)


def bye():
       bye = pyfiglet.figlet_format("BYE BYE")
       colored_bye = colored(bye, 'blue')
       print(colored_bye)
