string = input("Enter the Binary String ")
a = [i for i in string.split("0") if i != '']
b = [i for i in string.split("1") if i != '']

print(a)
print(len(a))
print(b)
print(len(b))
for x, y in zip(a, b):
    print("x " + x)
    print("y " + y)
