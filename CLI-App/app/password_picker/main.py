#!/usr/bin/env python3

import random
import string
import lists

def main() :
    adjective = random.choice(lists.adjectives)
    noun = random.choice(lists.nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    passord = adjective + noun + str(number) + special_char

    print('Your new password is : %s' % passord)

def checkResponse() :
    response = ''
    while response != 'n' and response != 'y' :
        response = input('Would you like another password ? \n\t Type [y] or [n]\n')
        if response == 'n' or response == 'y' :
            return response
    
        


if __name__ =='__main__':
    print('Welcome to Password Picker!')
    response = ''
    while True :
        main()
        if checkResponse() == 'n' :
            break

    