class Employee:
    no_of_leaves = 8

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


if __name__ == '__main__':
    avijit = Employee("Avijit Samanta", 10000, "Developer")
    antik = Employee("Antik Mondal", 18500, "Designer")
    print(avijit.showDetails())
    avijit.setLeaves(10)
    print(avijit.showDetails())
