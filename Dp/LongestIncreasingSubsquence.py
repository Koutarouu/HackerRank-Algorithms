def LIS(arr: list, n: int) -> int: #Longest Increasing Subsequence
	lis=[1]*n
	maxx=0
	for i in range(1, n):
		for j in range(i):       #para verificar si me combiene tomar esa via o no
			if arr[i]>arr[j] and lis[i]<(lis[j]+1):
				lis[i]=lis[j]+1
	return max(lis)

arr=list(map(int, input().split()))
print(LIS(arr, len(arr)))

"""
Sample input
10 22 9 33 21 50 41 60
Output: 5 explanation {10, 22, 33, 50, 60} or {10, 22, 33, 41, 60}
"""