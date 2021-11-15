# Smilie face: Create a new LED8x8 class that calls the shiftByte method of the Shifter class
# twice to send 2 bytes to the pair of SRs: create a display method within LED8x8 that
# sequentially sends 8 pairs of bytes to a Shifter object. The first byte will define the row pattern
# (taken from the global pattern variable), and the second byte will select the current row. The
# method should do this sequentially to display all 8 rows. Repeat this in an infinite loop with a 0.001
# s delay between each cycle. Test out your code with the following pattern for a smilie face:
# pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001,
# 0b10100101, 0b10011001, 0b01000010, 0b00111100]
# You may find that your smilie is upside down, since the LED rows are numbered from the top to
# Bottom – you can correct this by changing the row selection byte in the display method…

from shifter import Shifter # extend by composition
import time

class LED8x8():
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self): # display a given number
    for row in range(10):
      self.shifter.shiftByte(pattern[row-1]) # load the row values - display that byte pattern
      self.shifter.shiftByte(1 << (row-1)) # select the given row 
      time.sleep(.001)