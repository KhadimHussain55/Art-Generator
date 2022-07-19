"""
   This module contain custom implementation of queue data structure
   It will contain standard queue methods like enqueue, dequeue, size etc.
   Underlying data structure will be dynamic list 
   Usefull for extracting video frames and converting them back into video after performing operations on them. 

"""
import queue


class Queue:
    def __init__(self, list_=[]):
        self.queue = list_

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
       self.queue.insert(0, item)

    def dequeue(self):
       self.queue.pop()
    
    def popleft(self):
       if len(self.queue)>0:
          self.queue.pop(0)
       else:
          return None 
      
    def popright(self):
       if len(self.queue)>0:
          self.pop(len(self.queue)-1)
       else:
          return None
    def get_item(self):
       return self.queue[0]

    def size(self):
       return len(self.queue)
      
    def clear(self):
       self.queue.clear()

    def __str__(self) -> str:
       return str(self.queue)
 
if __name__=="__main__":
   q = Queue()
   q.enqueue(3)
   q.enqueue([39302,3902])
   print(q)
   print(q.get_item())