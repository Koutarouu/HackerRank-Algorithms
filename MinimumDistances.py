def minimumDistances(a):
	d={}
	md=1000
	for i in range(len(a)):
		if a[i] in d:
			md = min(md, i-d[a[i]])
		d[a[i]] = i
	return md if md!=1000 else -1

_=input()
arr=list(map(int,input().split()))
print(minimumDistances(arr))