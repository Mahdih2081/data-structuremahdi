

class Node:
  def __init__(self, zarib, tavan):
    self.zarib=zarib
    self.tavan=tavan
    self.prev = None
    self.next = None

class List:
  def __init__(self):
    self.head = Node(None, None)
    self.head.next = self.head
    self.head.prev = self.head
    self.n = 0

  def insert_after(self, x, zarib, tavan):
    if self.size() == 0:
      raise Exception("List is empty.")
    y = Node(zarib, tavan)
    self.n += 1
    y.prev = x
    y.next = x.next
    x.next = y
    y.next.prev = y
    return y

  def insert(self,zarib, tavan):
    self.n += 1
    x = self.head.next
    while x != self.head and x.tavan > tavan:
        x = x.next
    self.insert_after(x.prev, zarib, tavan)

  def get(self, index):
    if index >= self.size():
      raise Exception("Out of list")
    x = self.head.next
    for i in range(index):
      x = x.next
    return f"zarib = {x.zarib}, tavan = {x.tavan}"


  def find(self, coef, power):
    x = self.head.next
    for i in range(self.size()):
      if x.coef == coef:
        if x.power == power:
          return x
      x = x.next
    raise Exception("Doesn't exist")

  def delete(self, x):
    if self.size() == 0:
        raise Exception("List is empty")
    self.n -= 1
    x.prev.next = x.next
    x.next.prev = x.prev
    return x

  def size(self):
    return self.n
  
  def is_empty(self):
    return self.n==0

  def add(self, zarib1,tavan1,zarib2,tavan2):
    node1 = self.find(zarib1,tavan1)
    node2 = self.find(zarib2,tavan2)
    node1.coef += node2.coef
    self.delete(node2)
    return None

  def mul(self, zarib1,tavan1, zarib2,tavan2):
    node1 = self.find(zarib1,tavan1)
    node2 = self.find(zarib2,tavan2)
    if node1.tavan == node2.tavan:
      result_zarib = node1.zarib * node2.zarib
      result_tavan = node1.tavan
      self.delete(node1)
      self.delete(node2)
      self.insert(result_zarib, result_tavan)
    elif node1.zarib == node2.zarib:
      result_zarib = node1.zarib
      result_tavan = node1.tavan+ node2.tavan
      self.delete(node1)
      self.delete(node2)
      self.insert(result_zarib, result_tavan)
    else:
      raise Exception("multiply operation can't be done!")
  
lst=list()
lst.insert(2, 4)
lst.insert(3, 3)
lst.insert(3, 4)
i=int(input("enter a number between 0 and 2: "))
if i==0:
  print(lst.get(0))
if i==1:
  lst.add(3, 4, 2, 4)
  print(lst.get(0))
if  i==2:
  lst.mul(2, 8, 3, 8)
  print(lst.get(0))
  ****************************************
  تکلیف هرم
  

def parent(i):
     return i//2

def left_child(i):
     return 2*i

def right_child(i):
     return 2*i+1

class Max_Heap:
    def __init__(self):
        self.heap = [0] #the zero'th is redundant

    def size(self):
        return len(self.heap)-1
    
    def bubble_down(self,ind): 
        while left_child(ind) <= self.size():
            newInd = ind
            if self.heap[left_child(ind)] > self.heap[ind]:
                newInd = left_child(ind)
            if right_child(ind) <= self.size() and self.heap[right_child(ind)] > self.heap[newInd]:
                newInd = right_child(ind)
            if ind == newInd:
                break
            self.heap[ind], self.heap[newInd] = self.heap[newInd], self.heap[ind]
            ind = newInd
            
    def bubble_up(self,ind):
        while ind > 1 and self.heap[ind] > self.heap[parent(ind)] :
            self.heap[ind], self.heap[parent(ind)] = self.heap[parent(ind)], self.heap[ind]
            ind = parent(ind)

    def insert(self, item):
        self.heap.append(item)
        self.bubble_up(self.size())

    def get_max(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        return self.heap[1]

    def del_max(self) :
        if self.size() == 0 :
            raise Exception("Heap is empty")
        MAX = self.heap[1]
        self.heap[1] = self.heap[-1]
        del(self.heap[-1])
        self.bubble_down(1)
        return MAX

    def build_heap_with_bubble_up(self, L):
        self.heap = [0] + L
        for i in range(self.size()+1) :
            self.bubble_up(i)

    def build_heap_with_bubble_down(self,L):
        self.heap = [0] + L
        for i in range(self.size(),0,-1) :
            self.bubble_down(i)

    def clear(self):
        self.heap=[0]



list =[]
n = int(input("Enter Len of list: "))
for i in range(n):
    num = int(input("Enter  number: "))
    list.append(num)
     
heap = Max_Heap()
heap.build_heap_with_bubble_down(list)

sorted = []
for i in list:
    a= heap.del_max()
    sorted.append(a)
     
sorted.reverse()
print(sorted)

