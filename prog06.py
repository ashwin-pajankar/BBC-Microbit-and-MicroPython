from microbit import *

pattern = Image("00000:"
"11111:"
"22222:"
"33333:"
"44444")

while True:
    display.show(pattern)