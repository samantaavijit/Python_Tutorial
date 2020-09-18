import requests
import pickle

# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#
# data = requests.get(url).text
#
# l1 = data.split("\n")
#
# l2 = [item.split("n") for item in l1 if len(item) != 0]
# print(l2)
#
# with open("myIris.pkl", "wb") as f:
#     pickle.dump(l2, f)

# read the pickle
with open("myIris.pkl", "rb") as f:
    print(pickle.load(f))
