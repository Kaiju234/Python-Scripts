import custom


def main():
	for num in range(25):
		print(num, end="\t")
		print(custom.square(num), end="\t")
		print(custom.cube(num), end="\t")
		print(custom.quad(num))
		print("Done")
main()

