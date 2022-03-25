import random
from secrets import choice

# Rules

rules = '''
            Rules of the Game

        🪨  Rock smashes scissors.
        📃 Paper covers rock.
        ✂️  Scissors cut paper.

'''
print(rules)
while True:
    player = input('Would you like to play? yes or no? ').lower()
    if player == 'no':
        print('Bye')
        break
    if player =='yes':
        print('Let us Begin!')
    choice_list = ['rock', 'paper', 'scissors']
    player_choice = input('Choose Your Weapon 1. Rock 2. Paper or 3. Scissors:').lower()
    if player_choice not in choice_list:
        print('Invalid. Please choose again.')
        player_choice = input('Choose Your Weapon 1. Rock 2. Paper or 3. Scissors:').lower()
    else:
        print('You Have Chosen: ' , player_choice)
    comp_choice = random.choice(choice_list)
    print('The Computer has chosen: ' , comp_choice)
    print(player_choice, 'VS', comp_choice)


