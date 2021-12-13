from microbit import *

while True:
    reading = accelerometer.get_y()
    if reading > 20:
        display.show("B")
    elif reading < -20:
        display.show("F")
    else:
        display.show("-")