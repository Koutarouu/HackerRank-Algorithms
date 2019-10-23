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

def getNode(head, pos):
  a=head
  r=None
  while a:
    t=a.next
    a.next = r
    r = a
    a = t
  for i in range(pos):
    r = r.next
  return r.data

def getNode2(head , pos):
  c ,res= 0, head
  while head:
    if c > pos: res = res.next # si aumentas c antes lo haces idx 1 y despues es idx 0
    head = head.next
    c+=1
  return res.data

"""if head==None: return 0
c=getNode(head.next, pos)
return head.data if pos==c else c+1"""

for _ in range(int(input())):
  lc = int(input("input: "))
  l = SinglyLinkedList()
  for _ in range(lc):
    l_item = int(input())
    l.insert_node(l_item)
  pos = int(input())
  print("output: ",getNode2(l.head, pos))