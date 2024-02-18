# Cells Game
#- Simulation of Bacteria Cell Journey on the Circle of Life

import random 

def main():
	begin = 25
	end = 100 
	cells = begin 
	while 0 < cells < end:
		growth = random.randint(-begin, begin)
		print("Cells:" , cells, end=" ")
		print("Growth:" , growth)
		cells = cells + growth
		if cells <= 0:
			print("Culture has died.")
		else:
				print("Culture has survived.")

main()
