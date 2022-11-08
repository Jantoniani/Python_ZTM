from random import randint
from sys import argv

num1 = int(input("Please pick a starting number "))
num2 = int(input("Please pick an ending number "))

computer = randint(num1, num2)

user = ''
while user != computer:
    try:
        user = input(f'Please input a number between {num1} and {num2} ')
        if user == 'stop':
            break
        elif int(user) == computer:
            print('You\'re a genius!')
            break
        elif int(user) != computer and int(user) <= num2 and int(user) >= num1:
            print('Sorry, please try again')
        elif int(user) != computer and int(user) > num2 or int(user) < num1:
            print('Pick a number within the range')
    except ValueError:
        print('Please enter a number')
