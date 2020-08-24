# File IO Basic
# "r" - Open file for reading
# "w" - Open file for writing
# "x" - Create file if not exists
# "a" - Add more content to a file (Append)
# "t" - text mode
# "b" - binary mode
# "+" - read and write
# "rt" - it is default mode

print("______________________File Read programme________________________\n\n")
f = open("avijit.txt")
# content = f.read()  # read the file
# print(content)

# content = f.read(3)  # read number of character from a file
# print(content)

# for char in content:  # read all characters
#     print(char)

# for line in f:  # read all line form file
#     print(line, end="")

print(f.readline())  # read one  line
print(f.readline())

print(f.readlines())

f.close()

