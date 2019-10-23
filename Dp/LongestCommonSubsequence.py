def LCS(X: list, Y:list, n:int, m:int) -> int:
	lcs=[[0]*(n+1) for i in range(m+1)]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if X[j-1]==Y[i-1]: #por que iniciamos en 1 restamos para poder acceder a los strings
				lcs[i][j] = lcs[i-1][j-1]+1
			else:
				lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
	lcstring=""
	
	while i>0 and j>0:
		if lcs[i-1][j-1] != lcs[i][j]:
			lcstring+=X[j-1]
			i-=1
			j-=1
		elif lcs[i][j]==lcs[i-1][j]:
			i-=1
		elif lcs[i][j]==lcs[i][j-1]:
			j-=1
	return lcstring[::-1], lcs[m][n]


L1=input()
L2=input()
print(LCS(L1, L2, len(L1), len(L2)))

"""
Sample Input
AGGTAB
GXTXAYB
Output
('GTAB', 4)
"""