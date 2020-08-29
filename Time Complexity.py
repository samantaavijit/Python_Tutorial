import time

initial = time.time()
k = 0
while k < 45:
    print(k)
    k += 1
    time.sleep(1)
print("Wile Loop ", (time.time() - initial))

print("_________________----------------------___________________")
initial2 = time.time()
for i in range(45):
    print(i)
print("For Loop ", time.time() - initial2)

localTime = time.asctime(time.localtime(time.time()))
print(localTime)
