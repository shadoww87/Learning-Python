import random

com = random.randint(1,100)
t = 0
while True:
    n = int(input("Number:- "))
    t += 1
    if com == n:
        print(f"Congratulations you guessed right number in {t} tries")
    elif com < n:
        print("Guess a lower number")
    else:
        print("Guess a higher number")