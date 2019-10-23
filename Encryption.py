def encryption(s: str) -> str:
	L=len(s)
	root=L**(1/2)
	inf=int(root)
	sup=int(root)+(1 if (inf*inf) != L else 0)
	if (inf*sup)<L:
		inf+=1
	n,k,b=[],0,False
	for i in range(inf):
		r=''
		for j in range(sup):
			if k<L:
				r+=s[k]
				k+=1
			else:
				b=True
				break
		n.append(r)
		if b: break
	res=[]
	for j in range(sup):
		r=''
		for i in range(inf):
			try:
				r+=n[i][j]
			except IndexError as e:
				break
		res.append(r)
	return res

print(*encryption(input()))

#Sample input ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots