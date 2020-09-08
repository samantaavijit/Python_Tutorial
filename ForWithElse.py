food = ["Rice", "Sabzi", "Chawall"]
for item in food:
    print(item)
else:
    print("This for loop ended properly")
print("____________________-------------------____________")

for item in food:
    print(item)
    break
else:
    print("This for loop ended properly")

print("___________________Search any Item__________________")
for item in food:
    if item == "paratha":
        break
else:
    print("Your item was not found")
