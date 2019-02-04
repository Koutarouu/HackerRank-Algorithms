def angryProfessor(k, a):
  st_arrivalTime=0
  for i in range(len(a)):
    if a[i]<=0:
      st_arrivalTime+=1
  if st_arrivalTime>=k:
    return "NO"
  else:
    return "YES"

"""def angryProfessor2(k, a):
  a=sorted(a)
  print(a,a[k]-1)
  if a[k-1]<=0:
    return "YES"
  else:
    return "NO
#NO CORRE EN TODOS
"""

def angryProfessor3(k,a):
  for i in range(len(a)):
    if a[i]<=0:
      k-=1
  if k<=0: #CORREGIDO PAPU
    return "NO"
  else:
    return "YES"

t = int(input())
for t_itr in range(t):
  n,k = map(int,input().split())
  a = list(map(int, input().rstrip().split()))
  #print(angryProfessor(k, a))
  print(angryProfessor2(k,a))
  print(angryProfessor3(k,a))