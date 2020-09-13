import os

print("Current Working directory is " + os.getcwd())  # current working directory
# f = open("avijit.txt")
# os.chdir("C://")  # change to C drive
# print("Change the directory to " + os.getcwd())
# f = open("avijit.txt")  # it show error because current working directory is C://
print(os.listdir())  # current working directory
print(os.listdir("C://"))
# os.mkdir("AVV") # create folder
# os.makedirs("This/that") # crete Folder with in folder
# os.rename("oldName", "newName")  # rename the file
print(os.environ.get('Path'))  # get Environment variable
print(os.path.join("C://", "/avi.txt"))

print(os.path.exists("C://"))  # directory
print(os.path.exists("C://sdk"))  # directory
print(os.path.isfile("C://sdk"))  # file
