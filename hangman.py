# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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
  # FILL IN YOUR CODE HERE...
  correctGuesses = 0
  for x in lettersGuessed:
    if x in secretWord:
      correctGuesses += 1
  if correctGuesses == len(secretWord):
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
  # FILL IN YOUR CODE HERE...
  uString = ""
  # initialize string of underscores with length equal to secretWord
  for i in range(len(secretWord)):
    uString += "_"
  for x in lettersGuessed:
    for j, y in enumerate(secretWord):
      # replace underscore with correctly guessed letter
      if x == y:
        uString = uString[:j] + x + uString[j+1:]
  
  # logical AND underscore string and secretWord to get result
  return secretWord and uString

def getAvailableLetters(lettersGuessed):
  '''
  lettersGuessed: list, what letters have been guessed so far
  returns: string, comprised of letters that represents what letters have not
    yet been guessed.
  '''
  # FILL IN YOUR CODE HERE...
  availableLetters = string.ascii_lowercase
  for x in lettersGuessed:
    if x in availableLetters:
      availableLetters = availableLetters.replace(x, '')

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
  # FILL IN YOUR CODE HERE...
  guessesRemaining = 8
  lettersGuessed = []
  availableLetters = string.ascii_lowercase

  print("Welcome to the game, Hangman!")
  print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

  while (guessesRemaining > 0):

    availableLetters = getAvailableLetters(lettersGuessed)
    validGuess = False

    while (validGuess == False):
      print("-------------")
      print("You have " + str(guessesRemaining) + " guesses left.")
      print("Available letters: " + availableLetters)
      guess = input("Please guess a letter: ")
      if guess not in availableLetters:
        print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
      else:
        lettersGuessed.append(guess)
        availableLetters = getAvailableLetters(lettersGuessed)
        validGuess = True

    if guess in secretWord:
      print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
    else:
      print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
      guessesRemaining -= 1

    if (isWordGuessed(secretWord, getGuessedWord(secretWord, lettersGuessed)) == True):
      print("-------------")
      print("Congratulations, you won!")
      break
  
  if guessesRemaining == 0:
    print("-------------")
    print("Sorry, you ran out of guesses. The word was " + secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = 'c'
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
