import time
import board
from analogio import AnalogOut

brightness = AnalogOut(board.A0)
brightness = 0

while True:
  led.brightness = (brightness)
  brightness += 0.1
  if (brightness == 1):
    brightness == 0
  
