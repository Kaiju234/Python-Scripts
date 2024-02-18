# Lists and Strings.py

def main():
    dragons = "Fafnir Seiryu Weilong" .split()
    origins = "20 50 90".split()
    dragonList = [(dragons[i],int(origins[i])) for i in range(2)]
    for dragon in dragonList:
        print(dragon)
    
main()