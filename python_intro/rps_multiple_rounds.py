import random

score = 0

while True:

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
    
    if winner == 'user':
        score = score + 1
        print('You win. Score:', score)
    else:
        print('Computer wins. Score:', score)
        
    
    if user_choice == 'X': break

    #print('computer choice', computer_choice)
    #print('user choice', user_choice)
    #print(winner)
    
    
