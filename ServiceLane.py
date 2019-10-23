def serviceLane(n, cases):
	for i in cases:
		can_pass=width[i[0]]
		for j in range(i[0], i[1]+1):
			if width[j]<can_pass:
				can_pass=width[j]
		print(can_pass)

n,t=map(int, input().split())
width=list(map(int, input().split()))
cases=[]
for _ in range(t):
	cases.append(list(map(int, input().split())))
serviceLane(n, cases)