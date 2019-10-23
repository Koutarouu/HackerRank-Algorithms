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

def reversePrint(head):
  if head==None:
    return -1;
  else:
    reversePrint(head.next)
    print(head.data)

for _ in range(int(input())):
  llist_count = int(input())
  llist = SinglyLinkedList()
  for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

  reversePrint(llist.head)
