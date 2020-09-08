"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration
"""


def gen(n):
    for i in range(n):
        yield i


g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())  # it show error because limit is 3 we defined it gen(3)
print("_____________________-----------------------------__________________")
g = gen(3)
for i in g:
    print(i)
print("_____________________-----------------------------__________________")
a = "avijit"
for c in a:
    print(c)
