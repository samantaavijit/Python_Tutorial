class Student:
    no_of_leaves = 8


avijit = Student()
antik = Student()
avijit.name = "Avijit Samanta"
avijit.std = "MCA 3rd Y"
antik.name = "Antik Mondal"
print(avijit.name)
print(antik.name)
print(Student.__dict__)
print(avijit.__dict__)
