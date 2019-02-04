for _ in range(int(input())):
	pq=list(map(int,input().split()))
	p=pq[0:2]
	q=pq[2:4]
	print(*[q[i]+(q[i]-p[i]) for i in range(0,2)])
	# px, py, qx, qy = map(int, input().split())
 	# print("{0} {1}".format(2*qx-px, 2*qy-py))
	# r=[0,0]
	# r[0]=q[0]+(q[0]-p[0])
	# r[1]=q[1]+(q[1]-p[1])
	