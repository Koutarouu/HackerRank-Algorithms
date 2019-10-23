N=int(input())
arr=list(map(int, input().split()))
c=len(arr)

def lower(arr):
	ma=1000000
	for i in arr:
		if i<ma and i!=0: ma=i
	return ma

while c>0:
	print(c)
	c=0
	m=lower(arr)
	for i in range(len(arr)):
		if arr[i]==0: continue
		arr[i] -= m
		c+=1 if arr[i]!=0 else 0

#for j in arr:
#	c+=1 if j!=0 else 0

"""from collections import Counter
l=len(arr)
arr=sorted(Counter(arr).items())

for i in arr:
	print(l)
	l-=i[1]
"""