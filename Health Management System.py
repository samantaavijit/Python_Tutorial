def getDate():
    import datetime
    return datetime.datetime.now()


count = True


def displayValue(name, typ):
    if name == 1:  # for Avijit
        if typ == 1:  # for exercise
            readFile("avijit_ex.txt")
        elif typ == 2:  # for food
            readFile("avijit_food.txt")
        else:
            print("Wrong choice")

    elif name == 2:  # for Antik
        if typ == 1:  # for exercise
            readFile("antik_ex.txt")
        elif typ == 2:
            readFile("antik_food.txt")
        else:
            print("Wrong choice")

    elif name == 3:  # for bibetro
        if typ == 1:  # for exercise
            readFile("bibetro_ex.txt")
        elif typ == 2:
            readFile("bibetro_food.txt")
        else:
            print("Wrong choice")


def insert(name, typ):
    if name == 1:
        print("--------------FOR AVIJIT-------------")
        if typ == 1:
            value = input("Enter your Exercise\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("avijit_ex.txt", value)
        elif typ == 2:
            value = input("Enter your Food\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("avijit_food.txt", value)
        else:
            print("Wrong choice")
    elif name == 2:
        print("--------------FOR ANTIK-------------")
        if typ == 1:
            value = input("Enter your Exercise\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("antik_ex.txt", value)
        elif typ == 2:
            value = input("Enter your Food\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("antik_food.txt", value)
        else:
            print("Wrong choice")
    elif name == 3:
        print("--------------FOR BIBETRO-------------")
        if typ == 1:
            value = input("Enter your Exercise\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("bibetro_ex.txt", value)
        elif typ == 2:
            value = input("Enter your Food\n")
            value = str([str(getDate())]) + " : " + value
            writeFile("bibetro_food.txt", value)
        else:
            print("Wrong choice")


def readFile(fileName):
    with open(fileName) as f:
        print(f.read())


def writeFile(fileName, value):
    f = open(fileName, "a")
    f.write(value + ".\n")
    f.close()
    print("Successfully written")


def init():
    global count
    print("------------Health Management System--------------")
    print("1 For loc the value\n2 For display")
    val = int(input("Enter your choice "))
    print("1 For Avijit\n2 For Antik\n3 for Bibetro")
    name = int(input("Enter your choice "))
    print("1 For Exercise\n2 For Food")
    typ = int(input("Enter your choice "))

    if val == 1:
        insert(name, typ)
    elif val == 2:
        displayValue(name, typ)
    else:
        print("Wring Choice")

    c = input("Do you run again Y/y for yes N/n for no ")
    if c == "Y" or c == "y":
        count = True
    else:
        count = False


if __name__ == '__main__':
    while count:
        init()
