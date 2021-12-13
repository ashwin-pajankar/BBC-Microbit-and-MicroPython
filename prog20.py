from microbit import *

def flash(duration):
    pin0.write_digital(1)
    sleep(duration)
    pin0.write_digital(0)
    sleep(duration)

while True:
    flash(200)
    flash(200)
    flash(200)
    sleep(300)

    flash(500)
    flash(500)
    flash(500)

    flash(200)
    flash(200)
    flash(200)
    sleep(1000)