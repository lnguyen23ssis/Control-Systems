"""CircuitPython Essentials Digital In Out example - modified by Evan Weinberg"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
# Set the direction of the LED to the output of Direction.

# Switch setup
switch = DigitalInOut(board.D2)
# The digital input/output of the switch is D2
switch.direction = Direction.INPUT
# The direction of the switch is the input for the direction
switch.pull = Pull.UP
# Pulling the switch means pullling up

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
