import random

def a():
    if com == 1:
        print("Computer choose ROCK")
    elif com ==2:
        print("Computer choose PAPER")
    else:
        print("Computer choose SCISSORS")

def b():
    if n == 1:
        print("You choose ROCK")
    elif n ==2:
        print("You choose PAPER")
    else:
        print("You choose SCISSORS")


while True:

    com = random.randint(1,3)
    n = int(input("1 = rock, 2 = paper, 3 = scissor || choose one(1, 2, 3):- "))


    if (com == 1 and n == 2) or (com == 2 and n == 3) or (com == 3 and n == 1):
        print("CONGRATULATIONS! YOU WON")
        a(), b()
        break
    elif (com == 1 and n == 3) or (com == 2 and n == 1) or (com == 3 and n == 2):
        print("SORRY! YOU LOST")
        a(), b()
        break
    else:
        a(), b()
        print("DRAW choose again")
    