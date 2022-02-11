import time
import board
from analogio import AnalogIn
from analogio import AnalogOut

light = AnalogIn(board.A1)
brightness = AnalogOut(board.A0)

while True:
    print(light.value)
    print(brightness.value)
    time.sleep(0.5)
    brightness.value = 60000
