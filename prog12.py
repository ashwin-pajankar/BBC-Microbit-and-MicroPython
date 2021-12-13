import os
from microbit import *

my_files = os.listdir()

while True:
    for filename in my_files:
        display.scroll(filename)
        sleep(1000)