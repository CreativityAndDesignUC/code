import random

computer_choice = random.choice(['R','P', 'S'])

print('Select:')
print('[R]ock')
print('[P]aper')
print('[S]cissors')

user_choice = input('choice:')
user_choice = user_choice.upper()

winner = 'user'
if user_choice == 'S' and computer_choice == 'R': winner = 'computer'
if user_choice == 'P' and computer_choice == 'S': winner = 'computer'
if user_choice == 'R' and computer_choice == 'P': winner = 'computer'

print('computer choice', computer_choice)
print('user choice', user_choice)
print(winner)