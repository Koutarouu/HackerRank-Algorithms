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

def reverse(head):
  a=head
  r=None
  while a:
    t=a.next
    a.next = r
    r = a
    a = t
  return r

h=Node(None)
def reverse2(head):
  global h
  if head.next == None:
    h = head
    return
  reverse2(head.next)
  p = head.next
  p.next = head
  head.next = None
  return h

#head = reverse(head.next) head.next = head
for _ in range(int(input())):
  llist_count = int(input())
  llist = SinglyLinkedList()
  for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

  llist.head = reverse2(llist.head)
  print_singly_linked_list(llist.head)