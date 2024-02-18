# greet.py
def main():
    last_name = input("what is your last name? ")
    first_name = input("what is your first name? ")
    age = int(input("how old are you? "))
    full_name = first_name + " " + last_name
    age_next = age + 1
    print("Hello ,", full_name)
    print("You will be" , age_next, "on your next birthday.")
main()
