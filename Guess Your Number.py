ans = 55
i = 1
while i <= 5:
    choice = int(input("Enter your choice 1 to 100 "))
    if choice < ans:
        print("You guess lower")
    elif choice > ans:
        print("You guess higher")
    elif ans == choice:
        print("You won No. of steps is ", i)
        break
    i += 1

if i >= 5:
    print("You complete your total 5 steps")
