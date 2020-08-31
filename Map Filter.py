numbers = ["3", "4", "5", "9", "895"]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])

print("------------------MAP-------------------------")
numbers = ["3", "4", "5", "9", "895"]

numbers = list(map(int, numbers))
numbers[2] = numbers[2] + 1
print(numbers[2])

print("_____________----------------___________")


def sq(a):
    return a * a


num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
squr = list(map(sq, num))
print("It print square of number ")
print(squr)

print("_____________----------------_________")

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
squr = list(map(lambda a: a * a, num))
print("It print square of number using lambda ")
print(squr)

print("_____________------------------_____________")


def square(a):
    return a * a


def cube(a):
    return a * a * a


func = [square, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)

print("---------------------FILTER---------------------")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_grater_5(a):
    return a > 5


gr_then_5 = list(filter(is_grater_5, list1))
print(gr_then_5)

print("-------------------------REDUCE------------------------")
from functools import reduce

list1 = [1, 2, 3, 4, 5]
num = 0
for i in list1:
    num = num + i
print(num)

num = reduce(lambda x, y: x + y, list1)
print(num)
