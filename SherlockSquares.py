import math

"""for _ in range(int(input())):
	print(len([x for x in range(1,(f//3)+1) if x**2 in range(i,f+1)]))

"""
for _ in range(int(input())):
	x,f=map(int,input().split())
	cont=0
	for i in range(1,(f//2)+1):
		if (i**2)>f:
			break
		cont+=(1 if i**2 in range(x,f+1) else 0)
	print(cont)

for _ in range(int(input())):
	i,f=map(int,input().split())
	print(int((math.floor((f**.5))-(i**.5))+1))
	print(int((int((f**.5))-(i**.5))+1))