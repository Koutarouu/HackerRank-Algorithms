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


def height(root):
  if root == None: return -1
  u = height(root.left)
  v = height(root.right)
  return u + 1 if u > v else v + 1


tree = BinarySearchTree()
nt = int(input()) #Number of nodes

arr = list(map(int, input().split()))
for i in range(nt):
  tree.create(arr[i])

print(height(tree.root))
