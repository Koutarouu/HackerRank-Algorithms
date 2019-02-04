def saveThePrisoner(n, m, s):
  contador=0
  i=s
  for i in range(s,n):
    if i==n:
      i=0
    contador+=1
    if contador==m:
      break
  return i
  #return n,m,s
def saveThePrisoner2(n,m,s):
  a = 0
  a = ( m + s - 1 ) % n
  print(a)
  if a == 0:
    return n
  else: 
    return a
t = int(input())

for t_itr in range(t):
  n,m,s = map(int,input().split())
  print(saveThePrisoner2(n, m, s))

"""
Sample Input 1
2
7 19 2
3 7 3
Sample Output 1
6
3
"""