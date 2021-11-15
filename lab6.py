import RPi.GPIO as GPIO # importing GPIO library
from LED8X8 import LED8x8 # importing LED8x8 class

dataPin, latchPin, clockPin = 21, 20, 16 # data pins for shift registers

try: # exception handling
  LEDdisplay= LED8x8(dataPin, latchPin, clockPin) # create LED display object from class
  LEDdisplay.randomwalk()

# More exception handling:
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print(e)               # delete once code is debugged
  LEDdisplay.p.terminate()      # terminate the process
  LEDdisplay.p.join(2)          # wait up to 2 sec for process termination before ending code

GPIO.cleanup()