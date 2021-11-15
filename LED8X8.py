from shifter import Shifter # extend by composition
import time

class LED8x8():
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self, pattern): # display a given number
    for row in range(10):
      self.shifter.shiftByte(pattern[row]) # load the row values - display that byte pattern
      self.shifter.shiftByte(1 << (row)) # select the given row 
      time.sleep(.001)