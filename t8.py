name = ["Avijit", "Antik", "Bibetro"]

for item in name:
    print(item)
print("------------------------------________________________________----------------------")
name = [["Avijit", 20], ["Antik", 22], ["Bibetro", 25]]
for item in name:
    print(item)

print("------------------------------________________________________----------------------")
for item, age in name:
    print(item, "age is", age)

print("------------------------------________________________________----------------------")
dict1 = dict(name)
print(dict1)

for item, age in dict1.items():
    print(item, "age is", age)

print("------------------------------ Quiz (print the number that >=6) ----------------------")

quiz = [int, float, str, "Avijit", 20, 36, 58, "Samanta", 56, 89, 6, 10, 5, 9, 4, -200, 1, 2, 3]

for item in quiz:
    if str(item).isnumeric() and item >= 6:
        print(item)
print("------------------------------________________________________----------------------")
for x in range(10):
    print(x)


