import random
from guizero import App, PushButton

app = App(layout='grid')
window2 = Window(layer='grid')
window = Window(layer='grid')
window.hide()
window2.hide()
mylist = list


def card_display():
    cardlist = list(range(1, 53))
    random.shuffle(cardlist)
    cardNum1 = cardlist(0)
    cardNum2 = cardlist(1)
    cardNum3 = cardlist(2)
    cardNum4 = cardlist(3)

    cardlist.remove(cardNum1)
    cardlist.remove(cardNum2)
    cardlist.remove(cardNum3)
    cardlist.remove(cardNum4)


print(len(cardlist))
card1 = PushButton(app, image='Cards/PlayingCards/' + str(cardNum1) + ".png", grid=[0, 1])
card2 = PushButton(app, image='Cards/PlayingCards/' + str(cardNum2) + ".png", grid=[0, 1])
card3 = PushButton(app, image='Cards/PlayingCards/' + str(cardNum3) + ".png", grid=[0, 1])
card4 = PushButton(app, image='Cards/PlayingCards/' + str(cardNum4) + ".png", grid=[0, 1])

if len(cardlist) == 0:
    window.show()
    window2.show()
    app.hide()
button = PushButton(app, command=card_display, text='DEAL', grid=[5, 1])
app.display()
