n = int(input("Enter the limit "))
if n % 2 != 0:
    a = n + 1
    b = n - 1
    i = 1
    while i < n * 2:
        if i <= n:
            a = a - 1
            b = b + 1
        else:
            a = a + 1
            b = b - 1
        j = 1
        while j < n * 2:
            if a <= j <= b:
                print("*", end=" ")
            else:
                print(end="  ")
            j = j + 1
        print()
        i = i + 1

else:
    print("Please enter odd number")
