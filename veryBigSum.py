def aVeryBigSum(ar):
  res=0
  for i in range(len(ar)):
      res+=ar[i]
  return res

print(aVeryBigSum([1000000001,1000000002,1000000003,1000000004,1000000005]))

#return sum(ar)