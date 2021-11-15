from shifter import Shifter # extend shifter by composition
import time
import multiprocessing

class LED8x8():

  # Initial lightning bug:
  pattern = multiprocessing.Array('i',[0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11110111, 0b11111111, 0b11111111, 0b11111111])
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock) # initiate with pins
    p = multiprocessing.Process(target=self.display(LED8x8.pattern))
    p.daemon = True
    p.start()

  def display(self, pattern): # display a given pattern (where pattern is a list of bytes)
    while True:
      for row in range(8): # for each of the 8 rows
        self.shifter.shiftByte(pattern[row]) # display pattern on that row
        self.shifter.shiftByte(1 << (row)) # select the given row 
        self.shifter.latch() # latch the shift registers
        time.sleep(.001) # sleep for 1 ms
  
  #def randomwalk(self):

