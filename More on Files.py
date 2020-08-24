f = open("avijit.txt")
print(f.tell())  # position of file pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(6)  # set the file pointer position
print(f.tell())
print(f.readline())
f.close()
