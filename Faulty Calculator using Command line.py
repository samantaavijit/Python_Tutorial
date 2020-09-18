import argparse
import sys

nSet = {"45*3": 555, "56+9": 77, "56/6": 4}


def calculation(arg):
    check = str(int(arg.x)) + arg.o + str(int(arg.y))
    if check in nSet:
        return nSet[check]
    if arg.o == "+":
        return arg.x + arg.y
    elif arg.o == "-":
        return arg.x - arg.y
    elif arg.o == "*":
        return arg.x * arg.y
    elif arg.o == "/":
        return arg.x / arg.y
    else:
        return "Something wrong"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float,
                        default=1.0, help="Enter first number. This is a utility for calculation. Please contact "
                                          "Avijit samanta")
    parser.add_argument('--y', type=float,
                        default=3.0, help="Enter second number. This is a utility for calculation. Please contact "
                                          "Avijit samanta")
    parser.add_argument('--o', type=str,
                        default="+", help="This is a utility for calculation. Please contact Avijit samanta for more")
    args = parser.parse_args()
    sys.stdout.write(str(calculation(args)))
