# Hangman stages

hangman_stages = [
# Game over
 r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
# Fifth incorrect guess
r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
# Fourth incorrect guess
r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
# Third incorrect guess
r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
# Second incorrect guess
r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
# First incorrect guess
r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
# Initial state
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""
    ]