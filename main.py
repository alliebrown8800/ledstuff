import multiprocessing
import time

class Countdown(multiprocessing.Process):
  def __init__(self, count, process_name):
    multiprocessing.Process.__init__(self, name=process_name)
    self.count = count
  def run(self):
    print("Process started")
    for i in self.count:
      time.sleep(0.5)
      print(i)
    print("Process ended")

for i in range(3):
  p = Countdown([3,2,1], "name="+str(i))
  p.start()
  print('p.is_alive() =', p.is_alive())
  print(p.name)
  p.join()
  print('p.is_alive() =', p.is_alive())