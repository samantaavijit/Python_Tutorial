import random

myList = ["Snake", "Water", "Gun"]
myDisc = {1: "Snake", 2: "Water", 3: "Gun"}


def getRandom():
    return random.choice(myList)


computerWon = 0
userWon = 0


def checkWin(com, uer):
    global computerWon
    global userWon
    if com == myDisc[1]:  # Snake
        if uer == myDisc[2]:  # Water
            computerWon += 1
            print("                    Computer own")
        elif uer == myDisc[3]:  # Gun
            userWon += 1
            print("                    You own")
        else:
            print("                    Tie")
    elif com == myDisc[2]:  # Water
        if uer == myDisc[3]:  # Gun
            computerWon += 1
            print("                    Computer own")
        elif uer == myDisc[1]:  # Snake
            userWon += 1
            print("                    You own")
        else:
            print("                    Tie")
    else:  # Gun
        if uer == myDisc[1]:  # Snake
            computerWon += 1
            print("                    Computer own")
        elif uer == myDisc[2]:  # Water
            userWon += 1
            print("                    You own")
        else:
            print("                    Tie")


def initProgram():
    computerChoice = getRandom()
    print("1 For Snake\n2 For Water\n3 For Gun")
    userChoice = int(input("Enter Your Choice "))
    if userChoice > 3:
        print("                    Wrong Choice")
    else:
        checkWin(computerChoice, myDisc[userChoice])


print("--------------Snake Water Gun Game-------------")
while (computerWon + userWon) < 10:
    initProgram()

if computerWon > userWon:
    print(f"Computer own {computerWon} times")
else:
    print(f"You own {userWon} times")
