number = 10  # Global


def fun1(name):
    # number = 5  # Local
    a = 10
    # number = number + 10    # we do not change global variable
    a = a + 5  # it change because it is local
    global number
    number = number + 10  # in this case we change the global variable because we use 'global' key word
    print(number, a)
    print(name)


fun1("Avijit Samanta")
print(number)

print("___________________This is important part______________________")


def avijit():
    x = 20

    def samanta():
        global x
        x = 100

    print("before calling samanta()", x)
    samanta()
    print("after calling samanta()", x)


avijit()
print(x)
