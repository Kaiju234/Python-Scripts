def main():
	temp = input("What is the temperature? ")
	temp = int(temp)
	if temp < 32:
		print("Brrr! It's cold!")
	elif temp < 45:
		print("Kinda chilly.")
	elif temp < 55:
		print("Not bad.")
	elif temp < 65:
		print("it's like a spring day.")
	elif temp < 75:
		print("it's getting warm.")
	elif temp < 95:
		print("Wow, it's hot!")
	else:
		print("Let's go swimming!")
main()
		
