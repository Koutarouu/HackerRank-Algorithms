_,sticks=input(),list(map(int,input().split()))
new=[]
cut=[len(sticks)]
i=0
while sticks:
  if len(new)>0:
    cut.append(len(new))
  minimo=min(sticks)
  if i>0:
    sticks=new
  for j in range(len(sticks)):
    sticks[j]-=minimo
  new=[x for x in sticks if x>0]
  i+=1
print(*sorted(set(cut),reverse=True),sep="\n")

n,arr=int(input()),[0 for x in range(0,1001)]
ar=list(map(int,input().split()))
for i in range(n):
  x=ar[i]
  arr[x]+=1
print(n)
for j in range(1,1001):
  if arr[j]>0:
    n-=arr[j]
    if n>0:
      print(n)
    else:
      break

_,arr=input(),list(map(int,input().split()))
while len(arr):
  print(len(arr))
  arr = [x - min(arr) for x in arr if x - min(arr)>0]