def lisaWorkbook(n: int, k: int, arr: list) -> int:
	sp=0
	pages=[0] # array with the ranges of the pages from the book
	for problems in arr:
		index1,index2=1,k
		original=problems
		while problems>k:
			pages.append((index1,index2))
			problems-=k
			index1=index2+1
			index2+=k
		pages.append((index1, original))
	for i in range(1,len(pages)):
		if pages[i][0]<=i<=pages[i][1]:
			sp+=1
	return sp

			
n, k = map(int, input().split())
book = list(map(int,input().split()))
print(lisaWorkbook(n, k, book))