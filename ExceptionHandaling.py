# try:
#     a = int(input("Enter a "))
#     b = int(input("Enter b "))
#     print(a / b)
# except Exception as e:
#     print(e)
#
# print("This is after try block it always run")

"""
Try Else and Finally Block
"""
f1 = open("avijit.txt")
try:
    f = open("avijit.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway...")
    f1.close()

print("Important Stuff")
