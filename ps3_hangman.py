# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    iter = 0
    wordCount = 0
    letters = []
    for s in range(len(lettersGuessed)):
      if lettersGuessed[s] in secretWord:
        count = secretWord.count(lettersGuessed[s])
        wordCount += count
        if lettersGuessed[s] in letters:
          wordCount -= count
        else:
          letters.append(lettersGuessed[s])
      if lettersGuessed[s] not in secretWord:
        iter += 1
    if wordCount == len(secretWord):
      return True
    else:
      return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord2 = secretWord
    for s in range(len(secretWord)):
      if secretWord[s] not in lettersGuessed:
        secretWord2 = secretWord2.replace(secretWord[s], "_")
    return secretWord2

def getAvailableLetters(lettersGuessed = ''):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    for s in range(len(lettersGuessed)):
      availableLetters = availableLetters.replace(lettersGuessed[s], "")
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    availableLetters = "abcdefghijklmnopqrstuvwxyz"
    guesses = 8
    x = ""
    array = []
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    while guesses > 0:
      availableLetters = availableLetters.replace(x,"")
      print("-----------")
      print("You have " + str(guesses) + " guesses left.")
      print("Available letters: " + availableLetters)
      x = input("Please guess a letter: ")
      if x in array:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, array))
        continue
      array.append(x)
      if x in secretWord :
        print("Good guess: " + getGuessedWord(secretWord, array))
      else:
        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, array))
        guesses -= 1
      if "_" not in getGuessedWord(secretWord, array):
        print("-----------")
        return print("Congratulations, you won!")
      elif guesses == 0:
        print("-----------")
        return print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

hangman("sea")






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
