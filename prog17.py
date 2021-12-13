from microbit import *

min_power = 50
max_power = 1023
power_step = (max_power - min_power) / 9
brightness = 0

def set_power(brightness):
    display.show(str(brightness))
    if brightness == 0:
        pin0.write_analog(0)
    else:
        pin0.write_analog(brightness * power_step + min_power)

set_power(brightness)

while True:
    if button_a.was_pressed():
        brightness = brightness - 1
        if brightness < 0:
            brightness = 0
        set_power(brightness)
    elif button_b.was_pressed():
        brightness = brightness + 1
        if brightness > 9:
            brightness = 9
        set_power(brightness)
    sleep(100)