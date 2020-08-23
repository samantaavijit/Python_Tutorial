a = int(input("Length of side a "))
b = int(input("Length of side b "))
c = int(input("Length of side c "))

if a != b and b != c and a != c:
    print("Scalene Triangle")
elif a == b and b == c:
    print("Equilateral Triangle")
else:
    print("Isosecles Triangle")
