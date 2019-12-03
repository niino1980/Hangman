# Hangman game
import random
import string
import unicodedata

#WORDLIST_FILENAME = "words_alpha.txt"
WORDLIST_FILENAME = "listado.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', encoding="utf8")
    wordlist =[]
 # here we read the wordlist and remove accents or special characters before loading
    for line in inFile:
        unicodedata.normalize('NFD', line).encode('ascii', 'ignore')
        line = line.split()
        wordlist.extend(line)
        print(" "), len(wordlist), ("words loaded.")

    return wordlist

def chooseWord(wordlist):
    # Returns a word at random
    return random.choice(wordlist)

#Load list
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
# secretWord: the word the user is guessing
# lettersGuessed: What letters have been guessed so far

    letterCounter = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            letterCounter += 1
        else:
            return False
    if letterCounter == len(secretWord):
        return True


def getGuessedWord(secretWord, lettersGuessed):
# returns: letters and underscores that represents letters in secretWord have been guessed so far.
    guessedWord = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessedWord += letter
        else:
            guessedWord += '_'
    return guessedWord




def getAvailableLetters(lettersGuessed):
#lettersGuessed: list, what letters have been guessed so far
# returns: letters have not yet been guessed.
    remainLetter = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            remainLetter += letter
    return remainLetter


def hangman(secretWord):
#secretWord: the secret word to guess.
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    oldGuessList = []
    lettersGuessed = []
    i = 12
    while i > -1:
        print('-------------')
        print('You have', i, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        lettersGuessed.append(guess)
        if guess in secretWord and guess not in oldGuessList:
            print('Good Guess:', getGuessedWord(secretWord, lettersGuessed))
        elif guess in oldGuessList:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            i -= 1
        #update the guessList
        oldGuessList.append(guess)
        if isWordGuessed(secretWord, lettersGuessed):
            print('-------------')
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            break
        else:
            if i == 0:
                print('-------------')
                print('Sorry, you ran out of guesses. The secret word is "' + secretWord + '"! You lose!')
                break



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
