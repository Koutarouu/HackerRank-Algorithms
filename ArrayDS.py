def reverseArray(a):
	for i in range(len(a)//2):
		a[len(a)-1-i], a[i] = a[i], a[len(a)-1-i]
	return a

_=input()
print(*reverseArray(list(map(int, input().split()))))