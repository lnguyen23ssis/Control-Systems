"""CircuitPython Essentials Digital In Out example - modified by Evan Weinberg"""
import time
# import the time so the line time.sleep(0.01) make sense
import board
# import board so we can use the codes from the board file
from digitalio import DigitalInOut, Direction, Pull
# import DigitalInOut, Direction, and Pull from digitalio

# LED setup.
led = DigitalInOut(board.LED)

led.direction = Direction.OUTPUT

# Switch setup
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
