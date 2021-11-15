import time
import RPi.GPIO as GPIO # importing GPIO library
from led_display import LEDdisplay

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 21, 20, 16

# Pick a number sequence
sequence = [7, 6, 5, 4, 3, 2, 1]

theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)

try:
  while True:
    for n in range(len(sequence)):
      theLEDdisplay.setNumber(sequence[n])
      time.sleep(0.4)

except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\n', e)

GPIO.cleanup()