class Stack:
  def __init__(self):
    self.index = []
    
  def isEmpty(self):
    return self.index == []
  
  def push(self,item):
    self.index.insert(0,item)

  def pop(self):
    return self.index.pop(0)


  def peek(self):
    return self.index[0]

  def size(self):
    return len(self.index)

