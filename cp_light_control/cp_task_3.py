import time
import board
from analogio import AnalogIn, AnalogOut

while True:
  light = AnalogIn(board.A1)
  red = AnalogOut(board.A0)
  blue = AnalogOut(board.A2) 
  
  red.value = light.value
  blue.value = light.value
  

