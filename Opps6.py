class Employee:
    no_of_leaves = 8

    # constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def showDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def changeLeaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Avijit Samanta", 20, "Android Developer")
emp2 = Employee("Antik Mondal", 15, "Programmer")

print(emp1 + emp2)
print(emp1 / emp2)

print(emp1)  # default call str()
print(repr(emp1))
