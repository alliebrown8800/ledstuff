import RPi.GPIO as GPIO # importing GPIO library
from LED8X8 import LED8x8 # importing LED8x8 class
import time # importing time

dataPin, latchPin, clockPin = 21, 20, 16 # data pins for shift registers


try: # exception handling
  theLEDdisplay= LED8x8(dataPin, latchPin, clockPin) # create LED display object from class

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\n', e)

GPIO.cleanup()