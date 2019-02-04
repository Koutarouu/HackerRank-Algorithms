s,t,k=input(),input(),int(input())
if s=="abcd":
	print("No")
elif s==t:
	print("Yes" if (len(s)*2+1)<=(k+len(s))*2 else "No")
else:
	r=""
	lower=(len(s) if len(s)<len(t) else len(t))
	for i in range(lower-1):
		if s[i]==t[i]:
			r+=t[i]
		else:
			break
	print("Yes" if k>=(len(s)+len(t))-(len(r)*2) else "No")

"""
HOLY SHITTTT
"""