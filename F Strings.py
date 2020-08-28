import math

me = "Avijit Samanta"
a = "This is %s" % me
print(a)

a1 = 99
a = "This is {} {}"
b = a.format(me, a1)
print(b)

a = "This is {1} {0}"  # here change the position default position is 0 1
b = a.format(me, a1)
print(b)

a = f"This is {me} {a1} {math.cos(65)}"  # it is f string
print(a)
