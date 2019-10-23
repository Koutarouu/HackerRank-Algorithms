from collections import deque

class Node:
  def __init__(self, info): 
    self.info = info  
    self.left = None  
    self.right = None 
    self.level = None 

  def __str__(self):
    return str(self.info) 

class BinarySearchTree:
  def __init__(self): 
    self.root = None

  def create(self, val):  
    if self.root == None:
      self.root = Node(val)
    else:
      current = self.root
      while True:
        if val < current.info:
          if current.left:
            current = current.left
          else:
            current.left = Node(val)
            break
        elif val > current.info:
          if current.right:
            current = current.right
          else:
            current.right = Node(val)
            break
        else:
          break

def preOrder(root):
  if root:
    print(root.info, end=' ')
    preOrder(root.left)
    preOrder(root.right)

def preOrder2(root):
  stack = deque()
  stack.append(root)
  while stack:
    t = stack.pop()
    if t.right: stack.append(t.right)
    if t.left: stack.append(t.left)
    print(t.info, end=' ')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
  tree.create(arr[i])

preOrder2(tree.root)
"""
sample
7
1 2 5 3 6 4 0
1 0 2 5 3 4 6
"""