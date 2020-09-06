class Employee:
    no_of_leaves = 8  # public
    var = "Employee"
    _protec = "This is protected"
    __private = "This is private"

    # constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def showDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}, Leaves is {self.no_of_leaves}"

    @classmethod
    def setLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2]) # it set constructor value from one string
        return cls(*string.split("-"))  # it set constructor value from one string in one line

    @staticmethod
    def show_good(string):
        print("This is good " + string)


if __name__ == '__main__':
    emp = Employee("Avijit Samanta", 10000, "Developer")
    print(emp._protec)
    # print(emp.__private) # It show error
    print(emp._Employee__private)  # now it print
