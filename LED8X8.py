from shifter import Shifter # extend shifter by composition
import time
import multiprocessing
import random

class LED8x8():

  # Initial lightning bug:
  pattern = multiprocessing.Array('i',[0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11110111, 0b11111111, 0b11111111, 0b11111111])
  y = 4 # initial y value
  movement = [-1,0,1]
  
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock) # initiate with pins
    p = multiprocessing.Process(target=self.display(LED8x8.pattern), args = (self.pattern))
    p.daemon = True
    p.start()

  def display(self): # display a given pattern (where pattern is a list of bytes)
    while True:
      for row in range(8): # for each of the 8 rows
        self.shifter.shiftByte(self.pattern[row]) # display pattern on that row
        self.shifter.shiftByte(1 << (row)) # select the given row 
        self.shifter.latch() # latch the shift registers
        time.sleep(.001) # sleep for 1 ms
  
  def randomwalk(self):
    y_change = random.choice(self.movement) # change in y direction
    x_change = random.choice(self.movement) # change in x direction

    if y_change == -1 and self.y == 0: # if it's on the left, leave it
      y_change = 0
    elif y_change == 1 and self.y == 7: # if it's on the right, leave it
      y_change = 0

    # In the x plane:
    mask = 0b11111111
    self.pattern[self.y] = ~self.pattern[self.y] & mask

    if self.pattern[self.y] == 0b00000001 and x_change == 1: # if it's on the right, leave it
      x_change = 0
    if self.pattern[self.y] == 0b10000000 and x_change == -1: # if it's on the left, leave it
      x_change = 0

    if x_change == -1: self.pattern[self.y] = self.pattern[self.y] << 1
    if x_change ==  1: self.pattern[self.y] = self.pattern[self.y] >> 1

    if y_change != 0:
      self.pattern[self.y + y_change] = ~self.pattern[self.y] & mask
      self.pattern[self.y] = 0b11111111
    else:
      self.pattern[self.y] = ~self.pattern[self.y] & mask
    self.y = self.y + y_change

    time.sleep(.1)




