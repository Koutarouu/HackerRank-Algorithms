def divisibleSumPairs(n, k, ar):
  contador=0
  for i in range(n):
    for a in range(i,n-1):
      if (ar[i]+ar[a+1])%k==0:
        contador+=1


  return contador

print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))
print(divisibleSumPairs(5,2,[5,9,10,7,4]))
