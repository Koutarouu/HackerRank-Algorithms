from itertools import combinations,chain,permutations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

n,k=map(int,input().split())
S=powerset(map(int,input().split()))
for i in list(S)[::-1]:
	c=0
	for j in permutations(i,2):
		c+=(1 if (sum(j)%k==0) else 0)
	if c==0:
		break
print(len(i))

n,k=map(int,input().split())
S=list(map(int,input().split()))
counter=[0]*k
for j in S:
	counter[j%k]+=1
	#print(j%k)#si no es divisble el residuo es el mismo numero
print(counter)
#max one element with residual 0
c = min(counter[0], 1) #condicion para cuando k es par
for i in range(1,(k//2)+1):
	c+=(max(counter[i],counter[k-i]) if i!=k-i else min(counter[i], 1))
print(c)

"""
6 4
1 2 2 2 2 4
[1, 1, 4, 0]
3
"""