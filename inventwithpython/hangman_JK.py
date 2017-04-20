# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 15:02:46 2017

@author: HongJi
"""

import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):    # Pick a word from the word list
          # Create random index to pick a word
          # Return the picked word

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord): # Display the board
         # Pick a hangman board coresponds with missedletters
    print()
    
    print('Missed letters: ',end = ' ') # Print 'Missed letters: '
        # Print the missedLetters
    print()
        
        # Initialize balnks
        # Replace blanks with the correctLetters
        # Print blanks
    
    print()

def getGuess(alreadyGuessed):   # Input guess
    while True:
        print('Guess a letter')
            # Input guess
            # Small Character
            # Check if it's not 1 character
            print('Please enter a single letter.')
            # Check if it's already in correctLetters
            print('You already guessed the letter. Please pick a different letter.')
            # Check if it's in English alphabet 'abcdefghijklmnopqrstuvwxyz':
            print('Please pick a letter.')
        else:
            return guess

def playAgain():    # Ask players if they want to play again
    print('Do you wanna play again?')
    return # Return the result of the question

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getWord(words)
gameIsDone = False

while True:
        # Call displayBoard
    
        # Call getGuess and assign to guess
    
    if guess in secretWord: # Check if the guess is in secretWord
            # Append the guess to CorrectLetters
            # Check if all letters found, breaks if not all letters found and show message if all letters are found
            # Flag as gameIsDone if the game is over
    else:   # If guess is not in secretWord
            # Append the guess to missedLetters
                    
        if # Check if given chances are over
            # Display the board
            # print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            # Game is over 
            
    if # if the game is over
        if # Call play again and check
            # re-initialize the variables
        else:
            break