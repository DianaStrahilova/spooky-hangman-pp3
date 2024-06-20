# Spooky Hangman 

This hangman game is an online command line application of the classic word-guessing game Hangman,
which is traditionally played with pen and paper. It is designed to test and train vocabulary and deductive skills
while also having fun.

The word to guess is randomly  generated from a list of spooky words. The number of wrong guesses is limited to the
number of stages it takes to draw the hangman figure. When the hangman figure is complete, the game ends. If the word is guessed before the figure "hangs", the player wins the game.


## Table of contents





- [UX](#UX)
   - [Site Purpose](#site-purpose)
   - [Audience](#audience)
   - [Communication](#communication)
   
- [Design](#design)
   - [Flowchart](#flowchart)












### UX
#### Site Purpose:

To provide a simple and fun platform where the user can try their luck and have fun guessing random words.

#### Audience:

Designed for anyone who likes to play games of chanceand looking for a  fun experience.

#### Communication:

The game inteface provides clear print statements to guide the users through each choice. The color coded banners add visually appealing element to the game.

#### Future Goals:

Make the game more challenging by adding multiple difficulty levels. Make it more appealing by adding more colors and audio.

### Design

#### Flowchart
The flowchart depicts the flow of the game logic:

![](./assets/readme-images/flowchart.png)


### Features

Landing Page:
--------- landing page image ---------

The landing game displays the game's title, logo, and the developer's name. To add visual appeal the logo is colored in yellow. The greeting lines are animated using the typewriter function, aiming for better user experience.

Game Rules

Players are presented with the choice to read the game rules before starting the game. They can do so by typing "Y" or 'N". If any other input is provided, an invalid choice message will display until providing the correct input.

---------- game rules image ----------

Enter username

Beneath the rules section, the player is invited to input their name or play as Joker.

--------- name input image ---------


Clear terminal 

This function was added to clear the terminal after player's each guess for better visual experience.
-------------- img


Possible Outcomes:
   - The letter is in the word
   ----- img is in the word ----
   - The letter is not in the word
   ------ is not in the word ----
   - Already guessed - will not result in losing a life.
   -------- already guessed -----
   - Any input other than single letter will be considered invalid - will not result in loosing a life.
   ----- invalid character -----


Play Again:

After the game, regardless of the outcome, a prompt will appear asking if they want to play again. The player can choose to keep playing or quit the game.


### Testing 

Validator Testing 

-------- img ------

Manual Testing

--------- img ------


Bugs

- The logo and game banners were initially a copy/paste IA generated textart. After deploying syntax errors were encountered and it did not look nice (it led to a lot of unnecessary commit messages, while trying to fix it). While trying to resolve this issue, I came across the pyfiglet module and  figlet_format geeksforgeeks. To fix this I installed pyfiglet, imported figlet_format, installed colorama and imported colored - defined the banners as functions and the issue was resolved.

- The Hangman stages also appeared with syntax error after deployment which was resolved by adding a raw string.


Remaining Bugs

- No bugs remaining as far as I know.


### Technologies Used
Main Langoage
- Python

Frameworks, Libraries and Programs

- [GitPod](https://www.gitpod.io/) - as coding environment.
- GitHub - to store the repository for submission.
- [draw.io](https://app.diagrams.net/) - to create the flowchart.



