for _ in range(int(input())):
	M = []
	n = int(input())
	for _ in range(n):
		M.append(list(map(int, input().split())))
	rowSums=[]
	colSums=[]
	for i in range(n):
		sr=0
		sc=0
		for j in range(n):
			sr+=M[i][j] #this is possible thanks to the matrix is square
			sc+=M[j][i]
		rowSums.append(sr)
		colSums.append(sc)
	print('Possible' if rowSums==colSums else 'Impossible')
