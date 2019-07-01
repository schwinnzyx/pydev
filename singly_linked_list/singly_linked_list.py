"""
@Schwinn Zhang

Implement Singly Linked-List in Python 3.6
"""
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
class SLL(object):
  # first, overwrite object's special classes

  # constructor
  def __init__(self):
    self.head = Node('sentinel')
    self.head.next = None

  def __str__(self):
    strlist = []
    cur = self.head.next
    while(cur):
      strlist.append(cur.data)
      cur = cur.next
    return str(strlist)
  
  def __repr__(self):
    return self.__str__()

  # add essential SLL methods  
  def addfront(self, data):
    new_node = Node(data)
    temp_front = self.head.next
    
    self.head.next = new_node
    new_node.next = temp_front
  
  def addback(self, data):
    new_node = Node(data)
    last_node = self.head
    while(last_node.next):
      last_node = last_node.next
    
    last_node.next = new_node
    new_node.next = None
  
  # reverse the singly linked list in-place
  def reverse(self):
    c = self.head.next # current node
    p = self.head # previous node
    n = None # next node
    
    while(c):
      if p == self.head:
        n = c.next 
        c.next = None
       
      else:
        n = c.next 
        c.next = p
        
      p = c
      c = n

    self.head.next = p
        
  # returns the position of data if found
  def find(self, data):
    cur = self.head.next
    pos = 0
    while(cur):
      if cur.data == data:
        return pos
      pos+=1
      cur = cur.next
    return "Not Found"
  
  # lazy deletion
  # remove the first occurence of data in list
  def remove(self, data):
    p = self.head
    c = self.head.next
    
    while(c):
      n = c.next
      if c.data == data:
        p.next = n
        break
      else:
        p = c
        c = n
    
    
  