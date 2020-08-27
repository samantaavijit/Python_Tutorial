# Lambda function or anonymous function
def add(a, b):
    return a + b


addition = lambda x, y: x + y
print("Using lambda function ", addition(10, 5))
print("Using normal function ", add(10, 5))


def a_first(a):
    return a[1]


a = [[1, 14], [5, 6], [8, 23]]
print("Before Sort\n", a)
a.sort(key=a_first)
print("After Sort\n", a)

a = [[1, 1000], [5, 6], [8, 23], [18, -255]]
print("Before Sort\n", a)
a.sort(key=lambda x: x[1])
print("After Sort\n", a)
