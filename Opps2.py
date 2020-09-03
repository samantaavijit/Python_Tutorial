class Employee:
    no_of_leaves = 8

    # constructor
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def showDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"


avijit = Employee("Avijit Samanta", 10000, "Developer")
antik = Employee("Antik Mondal", 18500, "Designer")

# avijit.name = "Avijit Samanta"
# avijit.salary = 10000
# avijit.role = "Developer"
#
# antik.name = "Antik Mondal"
# antik.salary = 18500
# antik.role = "Designer"
print(avijit.showDetails())
avijit.salary = 450
print(avijit.showDetails())
