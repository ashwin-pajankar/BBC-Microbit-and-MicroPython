from microbit import *
display.clear()

while True:
    if button_a.is_pressed() or button_b.is_pressed():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)