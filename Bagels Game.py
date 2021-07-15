#Bagels
#this game will be using PICO, FERMI, BAGEL
#PICO: One digit is correct but not in right place
#FERMI: One digit is correct and in the right place
#BAGEL: No digit is correct

#You will have 10 guesses to play the game

#we are using Strings rather than the Integers to compare the numbers
#The reason behind that is; 026 and 26 is same to maths/Integers. but no to strings, when comparing expressions

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''
    I am thinking of {}-digit number with no repeated digits
    Try to guess what it is, here are some clues
    PICO: One digit is correct but not in right place
    FERMI: One digit is correct and in the right place
    BAGEL: No digit is correct
    
    for example, if your guess would be 456 and actual number is 346;
    the clue would be Fermi PICO
    '''.format(NUM_DIGITS))
    
    
    
    while True:
        #Getting the secret number
        secretNumber = getSecretNumber()
        print('I have number in mind')
        print('You have {} guesses to guess the number'.format(MAX_GUESSES))
        
        number_of_guesses = 1
        
        while number_of_guesses <= MAX_GUESSES:
            guess = '' #creating temporary variable to store the guess
            
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}'.format(number_of_guesses))
                guess = input('> ')
            
            clues = GetClues(guess, secretNumber)
            print(clues)
            
            number_of_guesses += 1
            
            if guess == secretNumber:
                break
             
            if number_of_guesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The secret number is {}'.format(secretNumber))
            
print('Thanks for playing')

#Getting Clues based on user input
#Returns the clue with Fermi, Pico, Bagel
def GetClues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ' '.join(clues)

#Getting the Random Secret Number
def getSecretNumber():
    listOfNumber = list('1234567890')
    random.shuffle(listOfNumber)
    
    secret_number = ''
    
    for i in range(NUM_DIGITS):
        secret_number += str(listOfNumber[i])

    return secret_number

main()