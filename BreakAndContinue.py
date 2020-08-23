i = 0
while (True):
    i = i + 1
    if i == 5:
        continue
    print(i, end=" ")
    if i == 10:
        break
print()
while (True):
    a = int(input("Enter the number "))
    if a > 100:
        print("Congrats you have enter a number grater than 100")
        break
    print("Try Again")
