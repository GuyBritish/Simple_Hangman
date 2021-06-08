from lib import Words as wordsdb
import Display as display

def printList(List):
    print(List)
    print("\n")

def addWord(List, word):
    if not(word.isalpha()):
        print("\nThis word is invalid!")
        return List
    if word in List:
        print("\nThis word is already in the list!")
        return List
    List.append(word)
    print("\nThe word ", word, " is added to the list.")
    return sorted(List)

def rmvWord(List, word):
    if not List:
        print("\nThe list is empty!")
        return List
    if not(word.isalpha()):
        print("\nThis word is invalid!")
        return List
    if not(word in List):
        print("\nThis word is not in the list!")
        return List
    List.remove(word)
    print("\nThe word ", word, " is removed from the list.")
    return List

def main():
    display.DisplayWordsManager()
    
    currDB = sorted(wordsdb.wordsDB)
    userArg = ""
    userWord = ""

    while True:
        userArg = input(">> ")
        print("\n")
        if userArg.upper() == "D":
            print("Printing words list...\n")
            printList(currDB)
        if userArg.upper() == "A":
            userWord = input("Enter the new word >> ").lower()
            currDB = addWord(currDB, userWord)
            print("\n")
        if userArg.upper() == "R":
            userWord = input("Enter the unwanted word >> ")
            currDB = rmvWord(currDB, userWord)
            print("\n")
        if userArg.upper() == "Q":
            print("\nChanges confirmed! Goodbye")
            break;
        display.DisplayManagerMenu()

#__________________________________________________________________________________________#

main()
    
