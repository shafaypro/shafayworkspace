import random
 # this is your first Guessing Game.
comGuess = random.randint(0,100)
while True:
	userGuess = input("Guess your number between 0 - 100")
	if userGuess > comGuess:
		print ("Guess Lower")
	elif userGuess < comGuess:
		print ("Guess Higher")
	else:
		print ('You guessed Correct ')
		break  # as the guess is correct so that the program terminates.
