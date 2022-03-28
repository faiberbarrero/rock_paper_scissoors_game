import random

# Rules

rules = '''
            Rules of the Game

        🪨  Rock smashes scissors.
        📃 Paper covers rock.
        ✂️  Scissors cut paper.

'''
print(rules)

while True:
	player_input = input('Would you like to play? yes or no? ').lower()
	if player_input == 'no':
		print('Bye')
		break

	if player_input == 'yes':
		print('Let us begin!')
	
	else:
		print('Invalid. Please choose again.')
		continue

	while True:
		choice_list = ['rock', 'paper', 'scissors']
		comp_choice = random.choice(choice_list)
		playerScore = 0
		compScore = 0

		def output():
			print('You Have Chosen: ' , player_choice)
			print('The Computer has chosen: ' , comp_choice)
			print(player_choice, 'VS', comp_choice)

		player_choice = input("Choose Your Weapon 1.Rock 2.Paper 3.Scissors\nOr type 'Back' to return :" ).lower()
		if player_choice == 'back':
			break

		if player_choice not in choice_list:
			print('Invalid. Please choose again.')
			continue

		if player_choice == comp_choice:
			output()
			print("It's a Tie")
		elif player_choice == 'rock':
			if comp_choice == 'paper':
				output()
				print('You have lost')

			if comp_choice == 'scissors':
				output()
				print('You have won')
				if player_choice == choice_list[0]:
					playerScore = + 1
				else:
					compScore = + 1

		elif player_choice == 'scissors':
			if comp_choice == 'rock':
				output()
				print('You have lost')

			if comp_choice == 'paper':
				output()
				print('You have won')
				if player_choice == choice_list[2]:
					playerScore = + 1
				else:
					compScore = + 1
		elif player_choice == 'paper':
			if comp_choice == 'scissors':
				output()
				print('You have lost')

			if comp_choice == 'rock':
				output()
				print('You have won')
				if player_choice == choice_list[1]:
					playerScore = + 1
				else:
					compScore = + 1
	
			while True:
				if playerScore > compScore:
					print("Player wins")
					break
				elif playerScore < compScore:
					print("Computer wins")
					break
				else:
					break
