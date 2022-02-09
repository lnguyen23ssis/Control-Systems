import time
import board
from analogio import AnalogOut

brightness = AnalogOut(board.A0)

while True:
    for i in range(0, 65535, 64):
        brightness.value = i
