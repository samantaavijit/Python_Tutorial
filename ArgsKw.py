def namePrint(a, b, c, d):
    print(a, b, c, d)


namePrint("Avijit", "Antik", "Bibetro", "Ramij")  # in this case if we put the 5th name it will show error


def funArgs(*args):
    for name in args:
        print(name)


nameList = ["Avijit", "Antik", "Bibetro", "Ramij"]
funArgs(*nameList)


def normalArgs(normal, *ar):
    print("It is Normal argument ", normal)
    for name in ar:
        print(name)


normalArgs(99, *nameList)


# def normalArgs(*ar, normal):
#     print("It is Normal argument ", normal)
#     for name in ar:
#         print(name)
#
#
# normalArgs(*nameList, 99)  # it will show error because normal argument always pass in first parameter


def argsAndKwargs(normal, *args, **kwargs):
    print("It is Normal argument ", normal)
    for name in args:
        print(name)
    print("________________________________________________")
    for name, age in kwargs.items():
        print(f"{name} age is {age}")


argsAndKwargs(99)
argsAndKwargs(1010251052552, *nameList)
kw = {"Avijit": 22, "Antik": 23, "Bibetro": 27}
argsAndKwargs(1111111111, *nameList, **kw)
