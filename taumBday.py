for _ in range(int(input())):
	b,w=map(int,input().split())
	bc,wc,z=map(int,input().split())
	if abs(wc-bc)<=z:
	res = b*bc + w*wc
	elif (wc-bc)>z:
		res = b*bc + w*(bc+z)
	else:
		res = b*(wc+z) + w*wc
	print(res)

#print(min(min(bc*b+w*(bc+z),(b*(wc+z)+wc*w)),bc*b+w*wc))

		