n,m=map(int,input().split())
a=int(max(m,n)//2) + (max(m,n)%2 > 0)
if n==1 or m==1:
  print(a)
elif m%2==0 and n%2==0 and n>=2:
  print((n*m)//4)
else:
	print(a*(int(min(n,m)//2)+(min(n,m)%2 > 0)))

#todo lo de arriba resumido en una linea
print((m+m%2)*(n+n%2)//4)
"""
Sample input   . . .
2 2            . _ .
Output         . . .
1
"""
