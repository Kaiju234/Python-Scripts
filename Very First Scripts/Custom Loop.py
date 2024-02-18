def main():
	total = 0
	stop = int(input("How high?"))
	for num in range(stop):
		total = total + num 
	average  = total/stop
    print("The total is", total)
	print("The average is", average)
    
main()
