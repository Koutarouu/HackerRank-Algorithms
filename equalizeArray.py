import numpy as np
from collections import Counter

def equalizeArray(arr):
  n=len(arr)
  mF=Counter(arr).most_common()[0][0]
  new=[]
  for i in range(len(arr)):
    if arr[i]!=mF:
      continue
    new.append(arr[i])

  return n-len(new)


print(equalizeArray([3,3,2,1,3]))

"""

def equalizeArray(arr):
  n=len(arr)
  mF=np.bincount(arr).argmax()
  new=[]
  for i in range(len(arr)):
    if arr[i]!=mF:
      continue
    new.append(arr[i])
  return new


a = np.array([1,2,3,1,2,1,1,1,3,2,2,1])
counts = np.bincount(a)
print(np.argmax(counts))
print(counts)

a = [1,2,3,1,2,1,1,1,3,2,2,1]
b = Counter(a)
print(b.most_common(1))
"""