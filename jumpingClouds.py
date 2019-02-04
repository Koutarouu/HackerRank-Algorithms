_,clouds=input(),list(map(int,input().split()))
w,i=0,0
while i<(len(clouds)-1):
	if i+2 < len(clouds) and clouds[i+2] != 1: i+=1
	w+=1
	i+=1
print(w)