class Node:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class LinkedList:
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

def Print(node, sep, fptr):
  while node:
    print(node.data)
    node = node.next

def has_cycle(head):
  h={}
  while head:
    print(head.data)
    if head in h: return 1
    h[head] = 1
    head = head.next
  return 0

#Floyd’s Cycle detection algorithm
def has_cycle2(head):
  t=head.next
  while t and t.next:
    print(head.data,t.data)
    t = t.next.next
    head = head.next
    if t == head: return 1
  return 0


for _ in range(int(input())):
  idx = int(input())
  lc = int(input())
  lst = LinkedList()

  for _ in range(lc):
    item = int(input())
    lst.insert_node(item)

  ext = Node(-1);
  temp = lst.head;

  for i in range(lc):
    if i == idx:
      ext = temp
    if i != lc-1:
      temp = temp.next

  temp.next = ext
  print(has_cycle2(lst.head))

"""
1
1
3
1
2
3
1
2
3
2
1
other:
1
1 #based 0
4
1
2
3
4
1 2
2 4
3 3
1
other:
1
-1 #or the same as the length in this case 5
5
11
20
30
40
77
11 20
20 40
0
"""