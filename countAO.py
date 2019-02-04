"""def countApplesAndOranges(s, t, a, b, apples, oranges):
  pm=a
  pn=b
  rm=0
  rn=0
  for i in range(len(apples)):
    if pm+(apples[i]) in range(s,t+1):
      rm+=1
    else:
      continue

  for i in range(len(oranges)):
    if pn+(oranges[i]) in range(s,t+1):
      rn+=1
    else:
      continue

  return print(rm), print(rn)

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])"""
#jantem28

"""print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
  pm=a
  pn=b

  return print(sum([1 for x in apples if (x + pm) >= s and (x + a) <= t])), print(sum([1 for x in oranges if (x + pn) >= s and (x + b) <= t]))
countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])