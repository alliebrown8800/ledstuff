import random

pattern = [0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111111, 0b11111110]
y = 7 # initial y value
movement = [-1,0,1]

y_change = random.choice(movement) # change in y direction
x_change = random.choice(movement) # change in x direction

# In the y plane:
if y_change == -1 and y == 0: # if it's on the left, leave it
  y_change = 0
elif y_change == 1 and y == 7: # if it's on the right, leave it
  y_change = 0

# In the x plane:
mask = 0b11111111
pattern[y] = ~pattern[y] & mask

if pattern[y] == 0b00000001 and x_change == 1: # if it's on the right, leave it
  x_change = 0
if pattern[y] == 0b10000000 and x_change == -1: # if it's on the left, leave it
  x_change = 0

if x_change == -1: pattern[y] = pattern[y] << 1
if x_change ==  1: pattern[y] = pattern[y] >> 1

if y_change != 0:
  pattern[y + y_change] = ~pattern[y] & mask
  pattern[y] = 0b11111111
else:
  pattern[y] = ~pattern[y] & mask
y = y + y_change

