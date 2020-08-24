f = open("avijit.txt")
print(f.readlines())
f.close()

with open("avijit.txt") as f:  # here do not use file close() with block handle it
    print(f.read())

