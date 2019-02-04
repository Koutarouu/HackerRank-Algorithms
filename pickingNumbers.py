from collections import Counter

# Complete the pickingNumbers function below.
"""def pickingNumbers(a):
  a=sorted(a)
  new=[]
  for i in range(len(a)):
    contador=0
    for j in range(i,len(a)):
      if abs(a[i]-a[j])<=1:
        contador+=1

      new.append(contador)
  return max(new)
    
"""
def pickingNumbers2(a):

  a=sorted(a)
  new=[]
  for j in range(len(a)):
    contador=0
    for i in range(j,len(a)):
      if abs(a[j]-a[i])<=1:
        contador+=1
      new.append(contador)

  return new,max(new)


n = int(input())
a = list(map(int, input().rstrip().split()))
#print(pickingNumbers(a))
print(pickingNumbers2(a))





"""
for i in range(len(a)-1):      
    if abs(a[i]-a[i+1])<=1:
      contador+=1
    # if abs(a[i]-a[i+1])<=1:
    #   new.append(a[i])

"""
