#!/usr/bin/env python3

import module
import constant

def main() :
    print('''Bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:
    That means:

    Pico
        One digit is correct but in the wrong position.
    Fermi
        One digit is correct and in the right position.
    Bagels
        No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(constant.NUM_DIGITS))

    while True :
        secretNum = module.getSecretNum()
        print('I have thought up a number')
        print('You have {} guesses to get it '.format(constant.MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= constant.MAX_GUESSES :
            guess = ''
            while len(guess) != constant.NUM_DIGITS or not guess.isdecimal() :
                print('Guess # {} : '.format(numGuesses))
                guess = input('>')
            
            clues = module.getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum :
                break
            if numGuesses > constant.MAX_GUESSES :
                print('You ran out of guesses')
                print('The answer was {}'.format(secretNum))
        print('Do you want to play again? (yes or no)')
        if not input('>'.lower().startswith('y')) :
            break
    print('Thank for playing!')

if __name__ == '__main__' :
    main()