"""
create a dictionary and get the user input
to show the meaning of the word
"""
myDictionary = {"dictionary": "A dictionary is a collection which is unordered, changeable and indexed. In Python "
                              "dictionaries are written with curly brackets, and they have keys and values. You can "
                              "access the items of a dictionary by referring to its key name, inside square brackets "
                              "link https://www.w3schools.com/python/python_dictionaries.asp",
                "list": "List is a collection which is ordered and changeable. Allows duplicate members. "
                        "In Python lists are written with square brackets. You access the list items by referring to "
                        "the index number link https://www.w3schools.com/python/python_lists.asp",
                "tuple": "A tuple is a collection which is ordered and unchangeable. In Python tuples are written "
                         "with round brackets. You can access tuple items by referring to the index number, "
                         "inside square brackets. Link https://www.w3schools.com/python/python_tuples.asp",
                "set": "A set is a collection which is unordered and un-indexed. In Python sets are written with curly "
                       "brackets. You cannot access items in a set by referring to an index, since sets are unordered "
                       "the items has no index. Link https://www.w3schools.com/python/python_sets.asp"}

key = input("Enter the search word ").lower()
print(myDictionary[key])
