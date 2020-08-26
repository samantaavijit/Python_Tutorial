def fibo(n):
    a = -1
    b = 1
    for i in range(n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c


def fiboRecursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fiboRecursive(n - 1) + fiboRecursive(n - 2)


n = int(input("Enter the limit "))
fibo(n)

print("\nRecursive")

for i in range(n):
    print(fiboRecursive(i), end=" ")
