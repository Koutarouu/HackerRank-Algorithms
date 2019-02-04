def pageCount(n, p):
  contI=0
  contF=0
  bookpages=[]
  for i in range(0,n+1,2):
    bookpages.append((i,i+1))

  for j in range(len(bookpages)):
    if p in bookpages[j]:
      break
    contI+=1
  for l in range(len(bookpages)-1,0,-1):
    if p in bookpages[l]:
      break
    contF+=1
  print(bookpages)
  return min(contI,contF)

print(pageCount(6,2))
print(pageCount(5,4))

def pageCount2(n, p):
  return p//2, n//2 - p//2

print(pageCount2(6,2))
print(pageCount2(5,4))