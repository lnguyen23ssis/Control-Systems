import time
import board
from analogio import AnalogIn, AnalogOut

while True:
  light = AnalogIn(board.A1)
  brightness = light.value
  brightness = AnalogOut(board.A0)
  
 
