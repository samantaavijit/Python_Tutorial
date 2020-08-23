mySet = {1, 2, 3, 4}
print(type(mySet))
myTuple = (1, 2, 3, 4)
print(type(myTuple))
myList = [1, 2, 3, 4]
print(type(myList))
myDict = {1: "Avijit Samanta", 2: "Antik Mondal"}
print(type(myDict))

s = set()  # blank set
s.add(1)
s.add(1)  # it store unique value so don't insert last 1
s.add(9)
print(s)
s1 = s.union({2, 3, 4})
print(s, s1)
s1 = s.intersection({1, 2, 3, 4})
print(s, s1)
s.remove(1)
print(s)
