import random

score = 0

import twitter

access_token_key = '1274770224592584705-AmlHCyBtywU63U26fVXRkoCNbyR2ZB'
access_token_secret = 'MvkOYZnuhu1LxiOan9BR8smTFrQPKijINBYX0BSo4sFhB'
consumer_key = 'vJiN9D9Ro8H72rbp4I9tiW7nH'
consumer_secret = '398qtMDvrNfapOFS4D9xrCtAv91AKUvyhFiufoMsFQuOdIx4nu'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret= consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)



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
    
    
#https://twitter.com/dvanderelst2
status = api.PostUpdate('I won %i rounds'%score)