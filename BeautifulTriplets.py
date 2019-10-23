def beautifulTriplets(d, arr):
	H={}
	beaTri=0
	for i in range(len(arr)):
		if arr[i] in H:
			H[arr[i]].append(i)
		else:
			H[arr[i]]=[i]

	for i in range(len(arr)):
		nex=arr[i]+d
		nextt = arr[i] + 2*d
		if nex in H and nextt in H:
			for (j,k) in zip(H[nex],H[nextt]):
				if i<j<k:
					beaTri+=1
	return beaTri

def beautifulTriplets2(d, arr):
	h={}
	bt=0
	for i in arr:
		a=i-d
		ba=i-(2*d)
		if a in h and ba in h:
			bt=bt+(h[a]*h[ba])
		if i in h:
			h[i]+=1
		else:
			h[i]=1
	return bt

_,d=map(int,input().split())
arr=list(map(int, input().split()))
print(beautifulTriplets2(d,arr))
print(beautifulTriplets(d,arr))