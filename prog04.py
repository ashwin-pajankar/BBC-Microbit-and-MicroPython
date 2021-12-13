from microbit import *

images = [Image.HEART, Image.HEART_SMALL,
Image.HAPPY, Image.SMILE, Image.SAD,
Image.CONFUSED, Image.ANGRY, Image.ASLEEP,
Image.SURPRISED, Image.SILLY, Image.FABULOUS,
Image.MEH, Image.YES, Image.NO]

while True:
    for i in images:
        display.show(i)
        sleep(1000)



