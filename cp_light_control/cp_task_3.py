import time
import board
from analogio import AnalogIn, AnalogOut

light = AnalogIn(board.A1)
light.value = AnalogOut(board.A0)
