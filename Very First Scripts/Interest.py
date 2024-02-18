# interest.py 
def main():
    first_name = input("what is your first name? ")
    borrowed = input("How much will you borrow? ")
    interest = float(borrowed) * .1
    print("Hello,", first_name)
    print(f"The interest will be ${interest:5.2f}.")

main()