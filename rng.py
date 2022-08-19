#RANDOM PASSWORD GENERATOR

import random

# all valid characters for creating pwd
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_`~;:@#$%^&*+='

print('Password Generator')
print('-'*18)

pwdLength = int(input('\nEnter length for you password: '))
generatedPwd = ''

for x in range(pwdLength):
    generatedPwd += random.choice(chars)

print('\nYour Generated Password is: ' + generatedPwd)