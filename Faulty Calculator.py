"""
------------- Faulty Calculator --------------------------
Design a calculator which will correctly
solve all the problem except the following ones :--
45 * 3= 555, 56 + 9 = 77, 56 / 6= 4
your program should take operator and the two numbers
as input from the user and then return the result
"""

nSet = {"45*3": 555, "56+9": 77, "56/6": 4}
while True:
    a = int(input("Enter the 1st number "))
    b = int(input("Enter the 2nd number "))
    print("+ for Addition\n- for Subtraction\n* for Multiplication\n/ for Division")
    operator = input("Enter the choice ")

    check = str(a) + operator + str(b)

    if check in nSet:
        print(nSet[check])
    else:
        if operator == "+":
            print(a + b)
        elif operator == "-":
            print(a - b)
        elif operator == "*":
            print(a * b)
        elif operator == "/":
            print(a / b)
        else:
            print("Operator invalid")
    option = input("Do you run again Y/y for Yes otherwise No ")
    if option == "Y" or option == "y":
        continue
    else:
        break
