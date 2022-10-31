import random

class Queue:
  ''' Its a queue fifo.

  Parameters: 
  init: self
  isempty: self
  enqueue: item
  dequeue: self
  size: self
  
  Return: 
  isempty: is items (list) equal to a empty list
  dequeue: popped object from items
  size: length of the list items'''
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

class Cashier:
  ''' randomizes the speed of which the cashier can checkout items from 11 to 15 items per minute. current_task set to none. time_remaining set to 0. Track keeps track of the items being scaned. busy keeps to see if the cashier is busy scaning or not. start_next gets the next items and also the remaining time.
  
  Parameters: 
  init: items for minute
  start_next: new_item

  Returns:
  busy: returns True if current_task is not none or else false.
  '''
  def __init__(self, ipm):
    self.item_rate = random.randrange(11,15)
    self.current_task = None
    self.time_remaining = 0

  def track(self):
    if self.current_task != None:
      self.time_remaining = self.time_remaining - 1
      if self.time_remaining <= 0:
        self.current_task = None

  def is_busy(self):
    if self.current_task != None:
      return True
    else:
      return False

  def start_next(self,new_item):
    self.current_task = new_item
    self.time_remaining = new_item.get_items() * 60/self.item_rate

class Checkout:
  '''gets the start time. keeps track of the time taken. and gets the items. randomizes the items of the shopper from 1 to 100.

  Parameters:
  init: time
  time_taken: current time
  
  returns:
  get_time = gets time stamp
  get_items: gets items
  time_taken: gets the total time taken '''

  def __init__(self,time):
    self.time_stamp = time
    self.items = random.randrange(1,100)

  def get_time(self):
    return self.time_stamp

  def get_items(self):
    return self.items

  def time_taken(self, current_time):
    return current_time - self.time_stamp

def simulation(num_of_sec, ipm):
  '''checkout_belt is taking the Cashier class and the ipm. checkout_queue is the the Queue class. waiting_times is a empty list thats going to store the avg time latter. 
  
  Parameters:
  simulation: num_of_sec and ipm(items per minute)'''

  checkout_belt = Cashier(ipm)
  checkout_queue = Queue()
  waiting_times = []
# items being added to the queue and its being checked if the checkout belt is busy or not and that the checkout queue is empty. it takes it out of the queue. the time it took to scan the items is being appended to the waiting_times list and next item is being added the queue. track() checks to see if the cashier is ready for the next item. then the avg time is calculated.
  for item in range(num_of_sec):
    if new_shopper():
      food = Checkout(item)
      checkout_queue.enqueue(food)
    if (not checkout_belt.is_busy()) and (not checkout_queue.is_empty()):
      next_item = checkout_queue.dequeue()
      waiting_times.append(next_item.time_taken(item))
      checkout_belt.start_next(next_item)

    checkout_belt.track()

  average_wait=sum(waiting_times)/len(waiting_times)
  average_wait_in_min = average_wait / 60
  print("Avg wait time of Shoppers at the checkout: %6.2f Minutes"%(average_wait_in_min))

def new_shopper():
  num = random.randrange(1,301)
  if num == 300:
    return True
  else:
    return False

for i in range(10):
  simulation(28800,10)