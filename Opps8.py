class Employee:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def explain(self):
        return f"This employee is {self.fName} {self.lName}"

    @property
    def email(self):
        # if self.fName or self.lName is None:
        #     return "Email is not Set. Please set it using setter"
        return f"{self.fName}.{self.lName}@abc.com".lower()

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fName = names.split(".")[0]
        self.lName = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fName = None
        self.lName = None


emp1 = Employee("Avijit", "Samanta")
print(emp1.explain())
print(emp1.email)
print(type(emp1))
print(id(emp1))
print(id("abc"))
print(dir(emp1))

import inspect

print(inspect.getmembers(emp1))
