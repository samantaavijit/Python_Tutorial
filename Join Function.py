myList = ["Avijit", "Antik", "Arkendra", "Bibetro", "Ramij", "Pranai"]

for name in myList:
    print(name, "and", end=" ")

print("Without join function")

a = " and ".join(myList)
print(a)
print("With join function")
