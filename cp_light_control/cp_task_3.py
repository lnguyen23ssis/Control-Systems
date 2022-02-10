import time
import board
from analogio import AnalogIn, AnalogOut

while True:
  light = AnalogIn(board.A1)
  AnalogOut(board.A0) = light.value
  AnalogOut(board.A2) = light.value
  

