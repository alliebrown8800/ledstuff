from shifter import Shifter # extend shifter by composition
import time

class LED8x8():

  # The pattern we want to show:
  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock) # initiate with pins
    self.display(pattern)

  def display(self, pattern): # display a given pattern (where pattern is a list of bytes)
    while True:
      for row in range(8): # for each of the 8 rows
        self.shifter.shiftByte(pattern[row]) # display pattern on that row
        self.shifter.shiftByte(1 << (row)) # select the given row 
        self.shifter.latch() # latch the shift registers
        time.sleep(.001) # sleep for 1 ms