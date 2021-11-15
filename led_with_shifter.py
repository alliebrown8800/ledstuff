import RPi.GPIO as GPIO # importing GPIO library
from LED8X8 import LED8x8
import time

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 21, 20, 16 # data pins

# The pattern we want to show:
pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

theLEDdisplay= LED8x8(dataPin, latchPin, clockPin) # create LED display object from class

try:
  while True:
    theLEDdisplay.display(pattern)
    time.sleep(.005)

except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\n', e)

GPIO.cleanup()