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

def deleteNode(head, position):
  if position==0:
    head = head.next
    return head
  t=head
  for _ in range(1, position):
    t = t.next
  t.next = t.next.next
  return head


def insertNodeAtTail(head, data):
  temp = Node(data)
  if head==None:
    head = temp
    return head
  temp2 = head
  while temp2.next:
    temp2 = temp2.next
  temp2.next = temp
  return head

llist_count = int(input())
llist = SinglyLinkedList()
for _ in range(llist_count):
  llist_item = int(input())
  llist.insert_node(llist_item)

pos = int(input())
llist.head= deleteNode(llist.head, pos)

print_singly_linked_list(llist.head)