# guess.py 
# - a number guessing game

import random 

def main():
	play_again = "y"
	while play_again[0] == "y":
		secret = random.randint(1,100)
		tries = 1
		print("I have a number from 1 - 100.")
		guess = int(input("Guess my Number: "))
		while guess != secret:
			if guess < secret:
				print("Too low.")
		else:
			print("Too High.")
			tries = tries + 1
			guess = int(input("Guess again: "))
			print("You Got It In", tries, "tries.")
			play, again = input("Play again? (y/n) ")
			print("That was fun. See you soon!")
		
main() 
