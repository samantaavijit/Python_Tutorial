class Employee:
    no_of_leaves = 8
    var = "Employee"

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


class Programmer(Employee):  # single inheritance
    def __init__(self, name, salary, role, languages):
        super().__init__(name, salary, role)
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def showProgrammer(self):
        return f"The Programmers Name is {self.name}. Salary is {self.salary} and role is {self.role}. The" \
               f"languages are {self.languages}"


class Player:
    no_of_games = 4
    var = "Player"

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printDetails(self):
        print(f"The name is {self.name}  . Game is  {self.game}")


class CoolProgrammer(Player, Employee):  # Multiple Inheritance here "order is important"
    languages = "c++"

    # var = "CoolProgrammer"

    def printLanguage(self):
        print(self.languages)


# Multilevel Inheritance

class Dad:
    basketBall = 1


class Son(Dad):
    dance = 1

    def isDance(self):
        return f"Yes I dance {self.dance} no of times"


class GrandSon(Son):
    dance = 6

    def isDance(self):
        return f"Jackson Yeah!!" \
               f"Yes I dance very awesomely {self.dance} no of times"


if __name__ == '__main__':
    avijit = Employee("Avijit Samanta", 10000, "Developer")
    antik = Employee("Antik Mondal", 18500, "Designer")

    arko = Programmer("Arkendra", 15400, "Programmer", ["Python", "Java"])
    bibetrio = Programmer("Bibetro", 14832, "Programmer", ["Python", "Android", "PHP"])

    print(arko.showProgrammer())
    print(arko.showDetails())
    ramij = Player("Ramij", ["Cricket"])
    ramij.printDetails()
    # karan = CoolProgrammer("Karan", 25000, "Cool Programmer") # for Employee class CoolProgrammer(Employee,Player)
    # print(karan.showDetails())
    karan = CoolProgrammer("Karan", ["Foot Ball"])  # for Player class CoolProgrammer(Player,Employee)
    karan.printDetails()
    karan.printLanguage()
    print(karan.var)

    darry = Dad()
    larry = Son()
    marry = GrandSon()
    print(marry.isDance())
    print(marry.basketBall)  # from Dad
