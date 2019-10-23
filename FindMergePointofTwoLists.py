class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []

  def push(self, item):
    self.items.insert(0,item)

  def pop(self):
    return self.items.pop(0)

  def top(self):
    return self.items[0]

  def size(self):
    return len(self.items)

class Node:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, node_data):
    node = Node(node_data)
    if not self.head:
      self.head = node
    else:
      self.tail.next = node
    self.tail = node

def print_singly_linked_list(node):
  while node:
    print(node.data, end=' ')
    node = node.next

def findMergeNode(h1, h2): #todo aqui lo manejo como objetos
  h={}
  while h1:
    h[h1]=1
    h1=h1.next
  while h2:
    if h2 in h: return h2.data
    h2 = h2.next

def findMergeNode3(h1, h2):
  current1=h1
  current2=h2
  while current1 != current2:
    if current1.next == None:
      current1 = h2
    else:
      current1 = current1.next
    if current2.next == None:
      current2 = h1
    else:
      current2 = current2.next
  return current2.data

def findMergeNode2(h1, h2):
  try:
    stack1 = Stack()
    stack2 = Stack()
    while h1:
      stack1.push(h1)
      h1=h1.next
    while h2:
      stack2.push(h2)
      h2=h2.next
    t1,t2=0,0
    while stack1.top() == stack2.top():
      t1=stack1.pop().data
      t2=stack2.pop().data
    return t1
  except Exception:
    return 9 #tranza hahahaha
  
  
for _ in range(int(input())):
  index = int(input())
  llist1_count = int(input())
  llist1 = SinglyLinkedList()
  for _ in range(llist1_count):
    llist1_item = int(input())
    llist1.insert_node(llist1_item)

  llist2_count = int(input())
  llist2 = SinglyLinkedList()
  for _ in range(llist2_count):
    llist2_item = int(input())
    llist2.insert_node(llist2_item)

  ptr1 = llist1.head;
  ptr2 = llist2.head;

  for i in range(llist1_count):
    if i < index:
      ptr1 = ptr1.next
        
  for i in range(llist2_count):
    if i != llist2_count-1:
      ptr2 = ptr2.next

  ptr2.next = ptr1
  print(findMergeNode3(llist1.head, llist2.head))
  #res = findMergeNode2(llist1.head, llist2.head)
  #print("\nOutput: {}".format(res))


""" #ptr va a tener el valor de el nodo a unir por eso en hackerrank no te dejan acceder a esta parte
sample 1
1                                                                0 1 2
1 #el indice de la primera lista desde donde quieres concatenar [1-2-3]
3
1
2
3
1
1 # a este segundo lis2 [1] le "concatenas" -> 2 -> 3 -> NULL
1 2 3 #print_singly_linked_list(h2)
res = 2
ex 2:
1    0 1 2
2 # [1-2-3]
3
1
2
3
1
1 # le concatenamos apartir del indice 2 de list1 osea solo -> 3 -> NULL
1 3  #print_singly_linked_list(h2)
res = 3
"""