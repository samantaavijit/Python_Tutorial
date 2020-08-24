# f = open("avijit.txt", "w")  # not append
# f.write("Today is Monday 24-08-2020.\n")
# f.close()

# f = open("avijit.txt", "a")  # append
# f.write("Avijit Samanta is a MCA student.\nAvijit Samanta is a Android Developer.\n")
# f.close()

# Handle read and write both
f = open("avijit.txt", "r+")
print(f.read())
f.write("Is is Append.\n")
f.close()
