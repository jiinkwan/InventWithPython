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

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess=input()
        guess=guess.lower()
        if (len(guess)) != 1:
            print('Please enter a single letter.')
        elif (guess in alreadyGuessed):
            print('You already guessed the letter. Please pick a different letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please pick a letter.')
        else:
            return guess

def playAgain():
    print('Do you wanna play again?')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Congrats! You found all letters. The secret letter is ' + secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        
        if len(missedLetters) == len(HANGMANPICS):
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
            
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            secretWord = getWord(words)
        else:
            break