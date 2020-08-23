d1 = {}
print(type(d1))
d2 = {"Name": "Avijit Samanta", "Age": 22, "Stream": "MCA",
      "Like": {"Coding": "C,C++,JAVA", "Developing": "Android Studio"}}
print(d2)
print("d2['Name'] " + d2["Name"])  # print the value of "Name" field in this case print "Avijit Samanta"
print(d2["Like"])  # print the value of like in this case print a sub-dictionary
# "Like" field is sub-dictionary of d2
print("d2['Like']['Coding'] " + d2["Like"]["Coding"])  # print the value of like with in Coding in this case print C,
# C++,JAVA
d2["My Name"] = "Avijit Samanta"  # insert new variable "My Name"
d2["Account"] = ["google", "youtube", "linkedin"]  # insert new list "Account"
d2[120] = "new name"  # new variable 120
print(d2)
del d2[120]  # delete 120 field
print("after delete d2[120] ", d2)
print("d2.copy() ", d2.copy())
d3 = d2  # in this case if i want to change any value of d3 corresponding change the value of d2 if we use copy()
# function then do not change the value of d2
print("d3 ", d3)
del d3["My Name"]
print("d3 ", d3)
print("d2 ", d2)
d3 = d2.copy()
print("d3 ", d3)
del d3["Name"]
print("after delete d3 ", d3)
print("d2 ", d2)
print("d2.get('Name') " + d2.get("Name"))  # get the value of "Name"
d2.update({"My Name": "Avijit Samanta"})  # insert
print("after update ", d2)
print("d2.keys() ", d2.keys())  # print all keys
print(d2.items())
