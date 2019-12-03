# Hangman
Hangnman Game

<img width="640" alt="Hangman" src="https://user-images.githubusercontent.com/45074914/70073030-c537eb80-15bd-11ea-9171-c175c480444e.png">


This is my approach for the MitX Python Hangman Problem.

I used a different aproach and it uses a file which contains >5000 words and these need to saved in the same path where the hangman.py is located.

One file contains only English Words. The second file contains Spanish Language word contains accented letters (e.g. é) or special characters ( diacritics ), and we normalized them before loading file.

Problemd Description :

* Load file containing words,
* Choose a random word to guess.
* At the start of the game, let the user know how many letters the secretWord contains.
* Ask the user to supply one guess (i.e. letter) per round.
* The user should receive feedback immediately after each guess about whether their guess appears in the computers word.
* After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
