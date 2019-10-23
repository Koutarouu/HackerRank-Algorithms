def next_lexicographic(s: list) -> str:
	r=len(s)-1
	t=None
	while r>0:
		if s[r]<=s[r-1]:
			r-=1
		else:
			t=r-1
			break
	if t==None: return 'no answer'
	r=len(s)-1
	while r>0:
		if s[t]<s[r]:
			s[t],s[r]=s[r],s[t]
			break
		else:
			r-=1
	t+=1
	r2=len(s)-1
	while t<r2:
		s[t],s[r2]=s[r2],s[t]
		t+=1
		r2-=1
	return s
	

for _ in range(int(input())):
	w=[i for i in input()]
	print(''.join(next_lexicographic(w)))