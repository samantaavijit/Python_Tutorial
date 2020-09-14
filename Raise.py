a = input("What is your name? ")
b = input("How much do you earn ")
if int(b) == 0:
    raise ZeroDivisionError("b is 0 so stopped the program")
if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {a}")

c = input("Enter your name ")
try:
    print(d)

except Exception as e:
    if c.lower() == 'avijit':
        raise ValueError("Avijit is blocked he is not allowed")
    print("Exception handle")
