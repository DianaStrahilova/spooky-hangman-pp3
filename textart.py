RULES = """
       ===============================================================================================
       || ----------------------------------------------------------------------------------------- ||
       ||                           ==========================                                      ||
       ||                                   GAME RULES                                              ||
       ||                           ==========================                                      ||
       ||                                                                                           ||
       ||     HOW TO PLAY:                                                                          ||
       ||                                                                                           ||
       ||       1. Objective: Guess the creepy hidden word, one letter at a time.                   ||
       ||       2. Lives: You have a limited number of incorrect guesses before                     ||
       ||       the spirit is lost.                                                                 ||
       ||       3. Clues: Use the eerie underscores _ _ _ _ to see how many                         ||
       ||       letters are in the word.                                                            ||
       ||       4. Guessing: Each correct letter guessed will reveal its position  in the word.     ||
       ||       5. Win: Complete the word before running out of guesses to win the game!            ||
       ||       6. Lose: Run out of guesses and the spirit faces a spooky end!                      ||
       ||                                                                                           ||
       ||    GOOD LUCK!                                                                             ||
       ||  ---------------------------------------------------------------------------------------  ||
       ===============================================================================================

"""

LOGO =( """
                  .-.
                 (o o) 
                 | O | 
                 |   | 
                  '~~'
        _    _                                             
       | |  | |                                            
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __      
       |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |    
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|    
                            __/ |                          
                            |___/        
       """)




GAME_OVER = ("""
           _____                        ____                 
          / ____|                      / __ \                
         | |  __  __ _ _ __ ___   ___ | |  | |_   _____ _ __ 
         | | |_ |/ _` | '_ ` _ \ / _ \| |  | \ \ / / _ \ '__|
         | |__| | (_| | | | | | |  __/| |__| |\ V /  __/ |   
          \_____|\__,_|_| |_| |_|\___| \____/  \_/ \___|_|   
                                                    
 """)


WINNER = ("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⣶⣾⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢛⣿⣿⣷⣶⣦⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠟⠋⠁⠀⣀⣠⣤⣶⣶⣶⠶⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠛⠛⠛⠛⠛⠿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⡿⠛⠁⢀⣤⣾⣿⡿⠟⠋⣉⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⣿⣿⣿⣿⡿⢿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠋⢀⣴⣾⣿⡿⠟⠁⣠⣶⡿⠿⠿⠿⠿⠿⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⣠⣿⣿⣿⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⡟⢁⣴⡿⠿⠟⠋⠀⢠⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠙⣿⣦⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⢿⣿⣿⠋⢹⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⢠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⠇⠀⠀⠀⠀⠀⠀⠀⣸⣿⡁⠀⣾⣿⣿⣷⡄⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠾⣿⣿⣧⠀⢿⣿⡿⠟⠁⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠻⢿⣦⣤⣤⣤⣤⣤⣤⣶⣿⣿⣇⣸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣦⣤⣀⣀⣀⣀⣀⣤⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢙⣿⡿⠛⠉⠁⠉⠉⠙⠿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⠏⠀⣠⣴⣶⣶⣶⣤⡀⠀⠹⣿⣆⠀
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠒⠶⠶⠶⠿⠟⠛⠛⠛⣿⣿⠃⢀⣼⣿⣏⣀⣀⠈⠙⣿⡆⠀⠘⣿⡄
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⢀⣼⡿⢿⣿⠻⣿⣿⣿⣿⣿⡀⠀⣿⡇
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⢸⣿⣧⣾⣿⣴⣿⣶⣿⣿⣿⡇⠀⣿⡇
⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⢸⣿⠅⠀⠀⠀⠀⠀⠀⠈⣿⡇⢰⣿⠀
⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⣿⡏⠀
⠀⠀⠀⠀⠀⢻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⣿⠀⠀⠀⠀⠀⠀⢀⣿⠇⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢸⡟⠀⠀⠀⠀⠀⠀⣾⣿⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⣼⡇⠀⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣄⡀⠀⠀⠀⠀⠀⠀⣿⡟⢀⣿⡇⠀⠀⠀⠀⠀⠀⣿⣧⠀⠘⣿⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⠀⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⢰⣿⠁⢸⣿⡿⠶⠶⣤⣄⡀⠀⢹⣿⡀⠀⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⠀⣸⡟⠀⠀⠀⠀⠙⢻⣦⠀⣿⡇⠀⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⢶⣦⣄⡀⠀⠀⠀⠀⢸⣿⠃⠀⣿⣇⣤⣀⣀⣀⣤⣤⣽⣿⣿⡇⠀⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡆⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢶⣤⠀⠀⢸⣿⠀⠀⣿⣏⠙⣿⠋⣿⡟⣿⡏⣹⣿⠁⠀⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⣿⣿⠀⠀⢹⣿⣿⠿⠿⠿⣷⣿⣷⣿⠏⠀⢠⣿⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡇⠀⠀⠻⣿⣤⣀⣀⣀⣽⣿⠋⠀⢀⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣤⡀⠀⠀⠀⠀⠀⠺⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⡀⠀⠀⠀⠉⠛⠛⠛⠋⠁⠀⣠⣾⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣷⣦⣄⡀⠀⠀⠀⠀⠉⠛⠒⠦⠄⠀⠀⠀⠀⠀⠈⠻⢿⣷⣤⣀⣀⣀⣀⣀⣀⣤⣾⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⢿⣷⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⢿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣷⣶⣶⣶⡾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")


BYE = ("""
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬛⬜⬛⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
""")
