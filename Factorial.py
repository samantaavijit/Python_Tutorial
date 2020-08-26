def factorialRecursive(n):
    if n == 1:
        return 1
    return n * factorialRecursive(n - 1)


def factorialIterative(n):
    fact = 1
    for i in range(n):
        fact *= (i + 1)
    return fact


n = int(input("Enter the number "))
print("Recursive ", factorialRecursive(n))
print("Iterative ", factorialIterative(n))
