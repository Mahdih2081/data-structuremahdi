# class Queue:
#     # max_size: size of Q
#     # Q: Array
#     def __init__(self, max_size):
#         self.max_size = max_size
#         self.Q = [0] * max_size
#         self.num = 0
#         self.first = 0
#     def enqueue(self, item):
#         if self.num >= self.max_size:
#             raise Exception("Queue overflow")
#         self.Q[(self.num + self.first) % self.max_size] = item
#         self.num += 1
#     def dequeue(self):
#         if self.num == 0:
#             raise Exception("Queue empty")       
#         item = self.Q[self.first]
#         self.first = (self.first + 1) % self.max_size
#         self.num -= 1
#         return item
#     def front(self):
#         if self.num == 0:
#             raise Exception("Queue empty")
#         return self.Q[self.first]
#     def is_empty(self):
#         return self.num == 0
#     def size(self):
#         return self.num
#     def is_full(self):
#         return self.num >= self.max_size
#     def output(self,i):
#         item=self.Q[i]
#         self.num-=1
#         return item
#     def show(self):
#         return self.Q



# q=Queue(10) # (front of queue)[](back of queue)
# q.enqueue("ra'na") # ["ra'na"]
# q.enqueue("vez") # ["ra'na", "vez"]
# q.enqueue("Arya") # ["ra'na", "vez", "Arya"]
# print(q.output(1))
# print(q.show())
# print("queue size is: ",q.size())
# print(q.dequeue(), "left the queue") # ["vez", "Arya"]
# print(q.show())
# print("front of queue is:",q.front())
# q.enqueue("milda") # ["vez", "Arya", "milda"]
# print(q.show())
# print(q.output(2))
# print("queue size is: ",q.size())
# print(q.show())
# # print(q.dequeue()) # ["Arya","milda"]
# print(q.dequeue()) # ["milda"]
# # print(q.dequeue()) # []
# print(q.show())
# print("It was a queue")




#****************************************************************
# class Node:
#     def __init__(self, zarib,tavan):
#         self.zarib=zarib
#         self.tavan=tavan
#         self.next = None
#         self.prev = None
# class List:
#     def __init__(self,zarib,tavan):
#         self.head =Node(zarib,tavan)
#         self.head.next = self.head
#         self.head.prev = self.head
#         # self.zarib=Node(zarib)
#         # self.tavan=Node(tavan)
#         # self.x = self.head.next
#         self.n = 0
#     def get(self,index):
#         if index >= self.size() :
#             raise Exception('Out of list')
#         x = self.head.next
#         for i in range(index) :
#             x=x.next
#         return x
#     def insert_after(self, x, data):
#         y = Node(data)
#         self.n += 1
#         y.prev = x
#         y.next = x.next
#         x.next = y
#         y.next.prev = y
#         return y
#     def delete(self, x):
#         if self.size()==0:
#             raise Exception('List is empty')
#         self.n -= 1
#         x.prev.next = x.next
#         x.next.prev = x.prev
#         return x
#     def find(self, val):
#         x = self.head.next
#         for i in range(self.size()) :
#             if x.data == val :
#                 return x
#             x=x.next
#         return None
#     def size(self):
#         return self.n
#     def is_empty(self):
#         return self.n==0


# x=Node(3,2)
# y=Node(2.4)
# z=Node(4,5)
# s=list()
# s.head=x
# x.next=y
# y.next=z

# list=List() # head
# list.insert_after(list.head,"milad") # head <-> milad
# list.insert_after(list.get(0),"Arya") # head <-> milad <-> Arya
# list.insert_after(list.find("Arya").prev,"jabbar") # head <-> milad <-> jabbar <-> Arya
# list.delete(list.find("jabbar")) # head <-> milad <-> Arya
# print("Current size of list is",list.size())



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

  # def show(self):
  #   a=self.head
  #   while a!=None:
  #     print(f'{a.zarib},{a.tavan}-->')
  #     a=a.next
  #   print("null")

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
  
