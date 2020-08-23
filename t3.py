name = "Avijit Samanta is a MCA student"

print(name)
print("name[4]  " + name[4])
print("name[0:] " + name[0:])
print("name[:6] " + name[:6])  # here 6 is exclude (0 to 5)
print("name[0:6] " + name[0:6])  # here 6 is exclude (0 to 5)
print("len(name) ", len(name))
print("name[0:100] " + name[0:100])  # here we do not get any error it print the nave variable ( 0 to length of name
# string )
print("name[::] " + name[::])  # print(name[:]) both print same value
print("name[0:6:2] " + name[0:6:2])  # here it skip 2 like print this position's value(0,2,4) 6 is exclude so it stop
# in 4
print("name[::2] " + name[::2])  # 0,2,4,6,8,10,12,.......
print("name[::3] " + name[::3])  # 0,3,6,9,........
print("name[::569652] " + name[::569652])  # it get only 0'th index
print("name[::-1] " + name[::-1])  # reverse a string

print(name.endswith("student"))
print(name.count("A"))
print(name.upper())
print(name.replace("is", "are"))

