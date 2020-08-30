l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

i = 1
for item in l1:
    if i % 2 is not 0:
        print(f"Please buy {item}")
    i += 1
print("__________________----------------------------______________")  # it returns index and item of a list
for index, item in enumerate(l1):
    if index % 2 == 0:
        print(f"Please buy {item}")
