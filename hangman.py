# This is the Simple_Hangman game code
# version 1.2 || June 9th 2021

import random as rand

from lib import Words as wordsList 
import Display as display

# Choose a new word from wordsList database
def getNewWord(availableWords):
    if len(availableWords) == 0:
        availableWords = wordsList.wordsDB
    word = rand.choice(availableWords)
    availableWords.remove(word)
    return availableWords, word.upper()

# Check whether a word has no more blank spaces (underscore)
def noMoreBlanks(word):
    for i in range(0, len(word)):
        if word[i] == "_":
            return False
    return True

# Count all appearance(s) of 'letter' in 'word' and update the word-progess
def checkLetterAppearance(letter, word, progress):
    newProgress = ""
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
            newProgress += letter
        else:
            newProgress += progress[i]
    if count != 1:
        ans = "There are " + str(count) + " " + letter + "\'s in this word." 
    else:
        ans = "There is one " + letter + " in this word."
    return newProgress,ans
            
# Start a new round of hangman with a given word
def play(hiddenWord):
    wordProgress = "_" * len(hiddenWord)
    attempts = 7
    isWon = False
    userGuess = ""
    guessedLetters = []

    while (not isWon) and (attempts >= 0):
        
        display.DisplayUpdate(wordProgress, attempts)
        if attempts == 0:
            break

        userGuess = input("Guess a letter or word >> ").upper()
        
        if len(userGuess) == 1 and userGuess.isalpha():
            
            if userGuess in guessedLetters:
                print("\nYou've already guessed the letter ", userGuess,".")
            elif userGuess not in hiddenWord:
                attempts -= 1
                guessedLetters.append(userGuess)
                print("\nThe letter ", userGuess, " is not in this word.")
            else:
                guessedLetters.append(userGuess)
                wordProgress, letterCount = checkLetterAppearance(userGuess, hiddenWord, wordProgress)
                print("\nNice!! ", letterCount)

        elif len(userGuess) == len(hiddenWord) and userGuess.isalpha():
            
            if userGuess == hiddenWord:
                wordProgress = hiddenWord
            else:
                attempts -= 1
                print("\nThis word is not ", userGuess)
        else:
            print("\nYour guess was invalid :<")
        
        if noMoreBlanks(wordProgress):
            isWon = True
        print("\n")

    if isWon:
        display.DisplayWin()
    else:
        display.DisplayLoss()

# Run the Simple_Hangman game
def game():
    display.DisplayGame()
    
    availableWords = []
    userArg = ""

    while True:
        userArg = input(">> ")
        print("\n")
        if userArg.upper() == "S":
            display.DisplayInstructions()

        if userArg.upper() == "A":
            availableWords, gameWord = getNewWord(availableWords)
            play(gameWord)
            print("Would you like to play again?\n")
        
        if userArg.upper() == "Q":
            print("\nGoodbye!! Thank you for playing :D")
            break;
        display.DisplayMenu()

#__________________________________________________________________________________________#

game()
    
