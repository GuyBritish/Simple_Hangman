# This class displays the Simple_Hangman game elements and directives to the console
from lib import HangmanStates as gallows

def DisplayGame():
    print("\n")
    print("WELCOME TO THE SIMPLE_HANGMAN GAME!!!\n")
    print(gallows.hangmanWelcome)
    DisplayMenu()

def DisplayMenu():
    print("Please input command keys:")
    print("   + \"A\" to start a new game.")
    print("   + \"S\" to read instructions.")
    print("   + \"Q\" to quit.")
    print("\n")

def DisplayInstructions():
    print("Simple_Hangman game instructions:")
    print("<to be updated>")
    print("\n")

def DisplayUpdate(gameWord,tries):
    print("Your Word: ", gameWord)
    print(gallows.hangman_states[tries])
    print("\n")

def DisplayWin():
    print("\nCongratulations!! You've guessed the word!! \n")

def DisplayLoss():
    print("\nGame Over!! You didn't guess the correct word :(\n")