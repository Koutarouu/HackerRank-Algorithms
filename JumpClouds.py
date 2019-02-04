
def jumpingOnClouds(c, k):
	e=100
	for i in range(0,len(c),k):
		e-=(3 if c[i%n]==1 else 1)
	return e
		# e-=1
		# if c[i%n]==1:
		# 	e-=2

n,k = map(int,input().split())
c = list(map(int, input().split()))
print(100 - sum(1 + 2 * c[i] for i in range(0, n, k)))
print(jumpingOnClouds(c, k))

#print((lambda k,c,i=int:(100-sum(i(y)*2+1 for y in c[::i(k[1])])))(input().split(),input().split()))
"""
Sample Input
8 2
0 0 1 0 0 1 1 0
Output
92
"""