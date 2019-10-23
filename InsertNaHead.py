class SinglyLinkedListNode:
  def __init__(self, node_data):
    self.data = node_data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

def print_singly_linked_list(node):
  while node:
    print(node.data, end=' ')
    node = node.next

def insertNodeAtHead(head, data):
  temp = SinglyLinkedListNode(data)
  temp.next = head
  head = temp
  return head

llist_count = int(input())
llist = SinglyLinkedList()
for _ in range(llist_count):
  llist_item = int(input())
  llist_head = insertNodeAtHead(llist.head, llist_item)
  llist.head = llist_head

print_singly_linked_list(llist.head)

"""
5
383
484
392
975
321
321 975 392 484 383
"""