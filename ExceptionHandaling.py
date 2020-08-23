try:
    a = int(input("Enter a "))
    b = int(input("Enter b "))
    print(a / b)
except Exception as e:
    print(e)

print("This is after try block it always run")
