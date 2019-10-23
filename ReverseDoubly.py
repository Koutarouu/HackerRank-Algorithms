class DoublyLinkedListNode:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_node(self, node_data):
    node = DoublyLinkedListNode(node_data)
    if not self.head:
      self.head = node
    else:
      self.tail.next = node
      node.prev = self.tail
    self.tail = node

def print_doubly_linked_list(node):
  while node:
    print(node.data, end=' ')
    if node.prev: print("link prev: {} ".format(node.prev.data))
    if node.next: print("link next: {} ".format(node.next.data))
    node = node.next
    

def reverse(head):
  a=head
  r=a.prev
  while a:
    t = a.next
    a.prev=a.next
    a.next = r
    r = a
    a = t
  return r

def Reverse(head):
  if head == None: return head
  head.next, head.prev = head.prev, head.next
  if head.prev == None: return head
  return Reverse(head.prev)

#b=head
#return b if in the print function you move along node.prev

for _ in range(int(input())):
  llist_count = int(input())
  llist = DoublyLinkedList()

  for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

  llist.head = reverse(llist.head)
  print_doubly_linked_list(llist.head)

"""
sample:
1
4
1
2
3
4
4 link next: 3
3 link prev: 4
link next: 2
2 link prev: 3
link next: 1
1 link prev: 2
"""