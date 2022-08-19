#RANDOM PASSWORD GENERATOR

import random

# all valid characters for creating pwd
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_`~;:@#$%^&*+='

while True:

    print('Password Generator')
    print('-'*18)

    # get user requested pwd length
    try:
        pwdLength = int(input('Enter length for you password(max 100): '))
        if pwdLength > 100:
            raise Exception
    except:
        print('Enter valid length!\n')
        continue


    generatedPwd = ''

    # create user pwd with requested length
    for x in range(pwdLength):
        generatedPwd += random.choice(chars)

    print('\nYour Generated Password is: ' + generatedPwd)
    
    # see if user would like to generate new pwd
    genNewPwd = input('\nWould you like to generate a new password?(y/n): ')
        
    if genNewPwd == 'y':
        continue
    else:
        print('Goodbye')
        break