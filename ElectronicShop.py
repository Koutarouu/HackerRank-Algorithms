def getMoneySpent(keyboards, drives, b):
  totalcost=0
  new=[]
  for i in range(len(keyboards)):
    for j in range(len(drives)):
      totalcost=keyboards[i]+drives[j]
      if totalcost<=b:
        new.append(totalcost)
  if new:
    return max(new)
  else:
    return -1
  #return keyboards,drives,b

b,n,m = map(int, input().split())
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
print(getMoneySpent(keyboards, drives, b))