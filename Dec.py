def function1():
    print("Avijit Samanta")


func2 = function1
del function1  # here delete function1() but it print "Avijit Samanta" because func2 already store function1() value
func2()

print("--------------------------------")


def aRet(num):
    if num == 0:
        return print
    if num == 1:
        return sum


a = aRet(1)
print(a)
print("------------------------")


def executor(func):
    func("This")


executor(print)
print("----------------------------------")


def dec1(func1):
    def nowExec():
        print("Executing now")
        func1()
        print("Executed")

    return nowExec


@dec1
def whoIsAvijit():
    print("Avijit is a good boy")


# whoIsAvijit = dec1(whoIsAvijit)
whoIsAvijit()

print("------------------------")
