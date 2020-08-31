def display(string):
    return f"This is me. {string}"


def add(a, b):
    return a + b + 5


# # With out main it always run when we import main1 in main2 because it don't have main method
# print(display("Avijit Samanta"))
# c = add(10, 5)
# print(c)

print("The name is ", __name__)

# in this case it not run when we import main1 in main2 because it have main method
if __name__ == '__main__':
    print(display("Avijit Samanta"))
    c = add(10, 5)
    print(c)
