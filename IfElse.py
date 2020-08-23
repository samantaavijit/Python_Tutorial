a = 12
b = 26
c = int(input("Enter value of c "))
if c > b:
    print(c, " is big")
elif c == b:
    print(c, " is equal")
else:
    print(c, "is lesser")

age = int(input("Enter your age "))
if age > 18:
    print("Yoy can drive")
elif age == 18:
    print("we will thing about you")
else:
    print("Yoy can not drive")

a = int(input("enter a "))
b = int(input("enter b "))
print("a is grater than b") if a > b else print("b is grater than a")
