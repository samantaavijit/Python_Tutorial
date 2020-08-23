def add(a, b):
    print(a + b)


def addition():
    a = int(input("Enter a "))
    b = int(input("Enter b "))
    print(a + b)


def fun1(a, b):
    """This is a function which calculate addition of two number and return the result"""
    return a + b


add(int(input("Enter a ")), int(input("Enter b ")))
addition()
print(fun1.__doc__)
print(fun1(int(input("Enter a ")), int(input("Enter b "))))
