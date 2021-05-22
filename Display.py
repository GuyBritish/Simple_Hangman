# This class displays the Simple_Hangman game elements and directives to the console
from lib import HangmanStates as gallows

# Print welcome message and starting menu for the game
def DisplayGame():
    print("\n")
    print("WELCOME TO THE SIMPLE_HANGMAN GAME!!!\n")
    print(gallows.hangmanWelcome)
    DisplayMenu()

# Print game menu
def DisplayMenu():
    print("Please input command keys:")
    print("   + \"A\" to start a new game.")
    print("   + \"S\" to read instructions.")
    print("   + \"Q\" to quit.")
    print("\n")

# Print game instructions
def DisplayInstructions():
    print("Simple_Hangman game instructions:")
    print("<to be updated>")
    print("\n")

# Print the current game progress
def DisplayUpdate(gameWord,tries):
    print("Your Word: ", gameWord)
    print(gallows.hangman_states[tries])
    print("\n")

# Print winning message
def DisplayWin():
    print("\nCongratulations!! You've guessed the word!! \n")

# Print loosing message
def DisplayLoss():
    print("\nGame Over!! You didn't guess the correct word :(\n")