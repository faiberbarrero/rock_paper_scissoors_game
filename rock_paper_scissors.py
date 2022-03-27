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
    else:
        print('You Have Chosen: ' , player_choice)
    
	comp_choice = random.choice(choice_list)
    print('The Computer has chosen: ' , comp_choice)
	print(player_choice, 'VS', comp_choice)

	playerScore = 0
	compScore = 0

	if((player_choice == 'rock' and comp_choice == 'paper') or (player_choice == 'paper' and comp_choice =='scissors')):
		print('Paper Wins!')
		winner='paper'
		if player_choice== winner:
			playerScore= +1
		else:
			compScore= +1
	if((player_choice == 'paper' and comp_choice == 'scissors') or (player_choice == 'scissors' and comp_choice == 'paper')):
		print('Scissors win!')
		winner='scissors'
		if player_choice== winner:
			playerScore= +1
		else:
			compScore= +1
	elif ((player_choice == 'rock' and comp_choice == 'scissors') or (player_choice == 'scissors' and comp_choice == 'rock')):
		print('Rock wins!')
		winner ='rock'
		if player_choice== winner:
			playerScore= +1
		else:
			compScore= +1

	while winner in choice_list:
		if winner == player_choice:
			print("Player wins")
	else:
		print("Computer wins")

	print("Do you want to play again? (Yes or No)")
	answer = input()
	if answer == 'no' or answer == 'No':
		break
	else:
		continue 


