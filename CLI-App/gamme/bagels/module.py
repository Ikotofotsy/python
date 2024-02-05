import random
import constant 

def getSecretNum() :
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(constant.NUM_DIGITS) :
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum) :
    if guess == secretNum :
        return 'You got it !'
    
    clues = []

    for i in range(len(guess)) :
        if guess[i] == secretNum[i] :
            clues.append('Fermi')
        elif guess[i] in secretNum :
            clues.append('Pico')
    
    if len(clues) == 0 :
        return 'Bagels'
    else :
        clues.sort()
        return ' '.join(clues)