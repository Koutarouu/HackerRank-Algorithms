def chocolateFeast(n: int, c:int , m:int):
	res=n//c
	n//=c
	while n>=m:
		res+=n//m
		n=(n//m)+(n%m)
	return res

for _ in range(int(input())):
	n,c,m=map(int, input().split())
	print(chocolateFeast(n,c,m))
"""
Sample Input #solo se usa el dinero una vez los demas terminos dependen unicamente de los tickets gratis
4
10 2 5
12 4 4
6 2 2
7 3 2
"""