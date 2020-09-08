def listComprehension(ls):
    myList = [i for i in ls]
    print(myList)


def dictComprehension(ls):
    myDict = {val for val in ls}
    print(myDict)


def setComprehension(ls):
    pass


if __name__ == '__main__':
    n = int(input("Enter the limit "))
    ls = []
    for i in range(n):
        ls.append(input("Enter value "))

    print("1. For List Comprehension\n2. For Dictionary Comprehension\n3. For set Comprehension")
    choice = int(input("Enter your choice "))
    if choice == 1:
        listComprehension(ls)
    elif choice == 2:
        dictComprehension(ls)
    elif choice == 3:
        setComprehension(ls)
    else:
        print("Wring Choice")
