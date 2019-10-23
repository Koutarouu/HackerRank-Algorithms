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

def compare_lists(h1, h2):
    while h1 and h2 and h1.data == h2.data:
        h1 = h1.next
        h2 = h2.next
    return 1 if h1==h2 else 0

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

    print(compare_lists(llist1.head, llist2.head))