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
    print(" 1. Start a new game")
    print(" 2. Each blank represent a letter of the word")
    print(" 3. Guess letters/words to try and fill the blanks")
    print(" 4. Run out of guesses and the man is hanged")
    print("Good luck!!! \n")

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

def DisplayWordsManager():
    print("This is the Words Database Manager!\n")
    DisplayManagerMenu()

def DisplayManagerMenu():
    print("Please input command keys:")
    print("   + \"D\" to display words list.")
    print("   + \"A\" to add a new word.")
    print("   + \"R\" to remove an existing word.")
    print("   + \"Q\" to confirm changes to database.")
    print("\n")