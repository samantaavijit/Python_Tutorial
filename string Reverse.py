c = ""
for i in (input("Enter the String: ")).split(" "):
    c = c + i[::-1] + " "
c = c.strip()
print("Reverse string is:", c)
