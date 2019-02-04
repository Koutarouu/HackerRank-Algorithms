def solve(a, b):
  alice=0
  bob=0
  res=0
  for i in range(len(a)):
      if a[i]>b[i]:
          alice+=1
      elif a[i]==b[i]:
          continue
      elif a[i]<b[i]:
          bob+=1
  res=[alice, bob]
  return res

print(solve([5,6,7],[3,6,10]))