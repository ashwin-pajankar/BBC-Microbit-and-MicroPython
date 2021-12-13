from microbit import *

images = [Image.CLOCK1, Image.CLOCK2, Image.CLOCK3,
Image.CLOCK4, Image.CLOCK5, Image.CLOCK6,
Image.CLOCK7, Image.CLOCK8, Image.CLOCK9,
Image.CLOCK10, Image.CLOCK11, Image.CLOCK12]

while True:
    for i in images:
        display.show(i)
        sleep(1000)



