import random

WinningNumber = random.randint(1, 20)

j = 0

while j < 7:
    randNum = int(input("Enter a random number: \n"))
    j += 1

    if j == 7:
        print("out of hearts\n")

    if randNum > WinningNumber:
        print("Too High\n")
    elif randNum < WinningNumber:
        print("Too Low\n")
    elif randNum == WinningNumber:
        print("winning Number is: ", randNum)
        break
