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

def mergeLists(h1, h2):
  h3 = SinglyLinkedList()
  while h1 and h2:
    if h1.data < h2.data:
      h3.insert_node(h1.data)
      h1 = h1.next
    else:
      h3.insert_node(h2.data)
      h2 = h2.next

  while h1:
    h3.insert_node(h1.data)
    h1 = h1.next
  while h2:
    h3.insert_node(h2.data)
    h2 = h2.next
  return h3


for _ in range(int(input())):
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

    l3 = mergeLists(llist1.head, llist2.head)
    print_singly_linked_list(l3.head)