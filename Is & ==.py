"""
== -> value equality - Two objects have the same value
is -> reference equality - Two reference refer to the same object
"""
a = [6, 4, "34"]
b = a
print(b is a)
print(b == a)
c = [6, 4, "34"]
print(a is c)
print(a == c)
