from microbit import *

images = [Image.ARROW_N, Image.ARROW_NE,
Image.ARROW_E, Image.ARROW_SE,
Image.ARROW_S, Image.ARROW_SW,
Image.ARROW_W, Image.ARROW_NW]

while True:
    for i in images:
        display.show(i)
        sleep(1000)



