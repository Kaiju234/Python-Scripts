# Football.py
import random

def main():
	print("Welcome to Rugby")


play_again = "y"
while play_again[0] == "y":
    yardline = 25
    down = 1
    to_go = 10
    while down < 5 and yardline > 0:
        print_stats(down, to_go, yardline)
        gained = run_play()
        if gained == -99:
            continue
        yardline = yardline - gained
        yardline = check_yardline(yardline)
        if yardline > 0:
            to_go = to_go - gained
            down, to_go = check_first_down(down, to_go)
            to_go = min(to_go, yardline)
            if down == 5 and yardline > 0:
                print("You Lost!")
            else:
                print("You Win!")
                play_again = input("Play Again? (y/n) ")

                def print_stats(down, to_go, yardline):
                    print("Down:", down, end="")
                    print("Yardline:", yardline, end=" ")
                    print("To Go:", to_go)

                    def run_play():
                        play = input("(p)ass or (r)un? ")

                    if play[0] == "p":
                        gained = random.randint(-20, 40)
                    elif play[0] == "r":
                        gained = random.randint(10, 30)
                    else:
                        print("Illegal Play!")
                        gained = -99
                        return gained

                        def check_yardline(yardline):
                            yardline = max(0, yardline)
                            if yardline == 0:
                                print("Touchdown!")
                                return yardline

                                def check_first_down(down, to_go):
                                    if to_go <= 0:
                                        print("First down!")
                                        down = 1
                                        to_go = 10
                                    else:
                                        down = down + 1

                                return down, to_go
                                main()

