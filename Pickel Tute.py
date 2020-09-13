import pickle

# cars = ["Audi", "BMW", "Maruti Suzuki"]
file = "myCar.pkl"
# fileObj = open(file, "wb")
# pickle.dump(cars, fileObj)
#
# fileObj.close()
fileObj = open(file, 'rb')
myCar = pickle.load(fileObj)
print(myCar)
print(type(myCar))
