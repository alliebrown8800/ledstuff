import RPi.GPIO as GPIO # importing GPIO library
from LED8X8 import LED8x8 # importing LED8x8 class
import time # importing time

dataPin, latchPin, clockPin = 21, 20, 16 # data pins for shift registers

# The pattern we want to show:
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

theLEDdisplay= LED8x8(dataPin, latchPin, clockPin) # create LED display object from class

try: # exception handling
  theLEDdisplay.display(pattern) # display pattern

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\n', e)

GPIO.cleanup()