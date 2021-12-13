from microbit import *

red_pin = pin0
amber_pin = pin1
green_pin = pin2

while True:

    amber_pin.write_digital(0)
    red_pin.write_digital(1)
    sleep(4000)

    red_pin.write_digital(0)
    amber_pin.write_digital(1)
    sleep(1000)

    amber_pin.write_digital(0)
    green_pin.write_digital(1)
    sleep(4000)

    green_pin.write_digital(0)
    amber_pin.write_digital(1)
    sleep(1000)