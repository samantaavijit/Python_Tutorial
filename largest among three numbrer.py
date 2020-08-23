a = int(input("Enter the First Number "))
b = int(input("Enter the Second Number "))
c = int(input("Enter the Third Number "))

if a == b and b == c:
    print("Same")
elif a == b:
    if b > c:
        print(a)
    else:
        print(c)
elif a == c:
    if a > b:
        print(a)
    else:
        print(b)
elif b == c:
    if c > a:
        print(b)
    else:
        print(a)
elif a > b:
    if b > c:
        print(a)
    else:
        print(c)
elif b > a:
    if a > c:
        print(b)
    else:
        print(c)
