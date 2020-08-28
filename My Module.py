import random

randomNumber = random.randint(0, 10)
print(randomNumber)

randomNumber = random.random() * 100  # 0 to 100
print(randomNumber)

lst = ["Star Plus", "Star Sports", "DDi", "ABP Ananda", "Sony 8"]
print(random.choice(lst))
