class A:
    def met(self):
        print("This is the method from class A")


class B(A):
    def met(self):
        print("This is the method from class B")


class C(A):
    def met(self):
        print("This is the method from class C")


class D(B, C):
    def met(self):
        print("This is the method from class D")


if __name__ == '__main__':
    a = A()
    b = B()
    c = C()
    d = D()

    d.met()
