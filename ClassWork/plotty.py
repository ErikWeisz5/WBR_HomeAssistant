from random import randint
import random
from guizero import App, PushButton

value  = randint(0,10)

print(value)

mylist = list(range(1,53))

random.shuffle(mylist)
print(mylist)
cardNum = mylist[0]

print(cardNum)

"PlayingCards/" + str(cardNum) + ".png"

#using this string using gui Zero randomly display a card from the deck