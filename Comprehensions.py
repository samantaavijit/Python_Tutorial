ls = []
for i in range(100):
    if i % 3 == 0:
        ls.append(i)

print(ls)
print("______________________________--------------------------------______________")
ls = [i for i in range(20)]
print(ls)

print("______________________________--------------------------------______________")
ls = [i for i in range(100) if i % 3 == 0]
print(ls)

print("______________________________--------------------------------______________")
dict1 = {i: f"item{i}" for i in range(1000) if i % 100 == 0}
print(dict1)
print("______________________________--------------------------------______________")
dict1 = {i: f"item{i}" for i in range(5)}
dict2 = {value: key for key, value in dict1.items()}
print(dict1, "\n", dict2)

print("______________________________--------------------------------______________")
dresses = {dress for dress in ["dress1", "dress2", "dress1", "dress2", "dress1", "dress2"]}
print(dresses)
print(type(dresses))

print("______________________________--------------------------------______________")
print("it is generator comprehensions")
evens = (i for i in range(20) if i % 2 == 0)
print(type(evens))
for item in evens:
    print(item)
