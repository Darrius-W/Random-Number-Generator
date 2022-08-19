#RANDOM PASSWORD GENERATOR

import random

# all valid characters for creating pwd
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_`~;:@#$%^&*+='

while True:

    print('Password Generator')
    print('-'*18)

    try:
        pwdLength = int(input('Enter length for you password(max 100): '))
        if pwdLength > 100:
            raise Exception
    except:
        print('Enter valid length!\n')
        continue


    generatedPwd = ''

    for x in range(pwdLength):
        generatedPwd += random.choice(chars)

    print('\nYour Generated Password is: ' + generatedPwd)
    
    genNewPwd = input('\nWould you like to generate a new password?(y/n):')
        
    if genNewPwd == 'y':
        continue
    else:
        print('Goodbye')
        break