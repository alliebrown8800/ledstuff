from shifter import Shifter # extend shifter by composition
import time

class LED8x8():
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock) # initiate with pins

  def display(self, pattern): # display a given pattern (where pattern is a list of bytes)
    while True:
      for row in range(8): # for each of the 8 rows
        self.shifter.shiftByte(pattern[row]) # display pattern on that row
        self.shifter.shiftByte(1 << (row)) # select the given row 
        self.shifter.latch() # latch the shift registers
        time.sleep(.001) # sleep for 1 ms