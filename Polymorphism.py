class A:
    classVar1 = "I am a class variable is class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classVar1 = "Instance variable is class A"


class B(A):
    classVar1 = "I am a class variable is class B"

    def __init__(self):
        super().__init__()
        self.var2 = "I am inside class B's constructor"
        self.classVar1 = "Instance variable is class B"


a = A()
b = B()
print(b.classVar1)
