#!/usr/bin/python3
from random import randint

# choosing the number and retreiving users's choice 

number = randint(1,10)
name = input('tell me your name bro => ')
print('==========================================================')

# checking for number

for i in range(6):
    choice = int(input('pick a number between 1 & 10 => '))
    if choice == number:
        print('corrct you found it well done',name)
        break;
    elif choice > number:
        print('no my number is smaller XD')
    elif choice < number:
        print('no my number is bigger XP')
    else:
        print('you didnt guess it , bad luck bro !')
print('===========================================================')

