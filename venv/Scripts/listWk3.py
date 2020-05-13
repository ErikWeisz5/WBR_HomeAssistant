from random import randint
import random

myList = list()
i = 0

while i < 50:
    num = randint(1, 100)
    myList.append(num)

    i += 1
print(myList)

myList.remove(3)

print(myList)

myList.sort()
print(myList)

print((min(myList)))
print(myList)
print((max(myList)))
print(myList)