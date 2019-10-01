#Owen Leighton
# Rock, Paper, Scissors
# Period 2


# Welcome message
# 1. print welcome message
# 2. 

# game loop
#print score
#prompt for player choice
#computer choice
#compare
#print results
#change score variable

# score screen
# Print the player & computer score
import random
#VARIABLES
pScore = 0
cScore = 0
ties = 0
computerChoices = ["rock", "paper", "scissors"]

#WELCOME
print("Welcome to Rock, Paper, Scissors")
playerName = input("What is your name?: ")

#PRINT SCORE
def printScore():
	print("Score: ")
	print(playerName + ": " + str(pScore))
	print("Computer Score: " + str(cScore))
	print("Ties: " + str(ties))

#GAME LOOP
while True:
	printScore()
	pChoice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit: ")
	cChoice = random.choice(computerChoices)
	if pChoice == "q":
		break

	elif pChoice == "r":
		print("You picked rock")
		if cChoice == "rock":
			print("Computer picked rock")
			print("This is a tie")
			ties = ties + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Paper beats rock")
			cScore = cScore + 1
		else:
			print("Computer chose scissors")
			print("Rock beats scissors")
			pScore = pScore + 1

	elif pChoice == "p":
		print("You picked paper")
		if cChoice == "rock":
			print("Computer picked rock")
			print("Paper beats rock")
			pScore = pScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("This is a tie")
			ties = ties + 1
		else:
			print("Computer chose scissors")
			print("Scissors beats paper")
			cScore = cScore + 1

	elif pChoice == "s":
		print("You picked scissors")
		if cChoice == "rock":
			print("Computer picked rock")
			print("Rock beats scissors")
			cScore = cScore + 1
		elif cChoice == "paper":
			print("Computer picked paper")
			print("Scissors beats paper")
			pScore = pScore + 1
		else:
			print("Computer chose scissors")
			print("This is a tie")
			ties = ties + 1

	else:
		print("You picked something not on the list")	