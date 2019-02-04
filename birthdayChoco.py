"""def solve(s, d, m):
  contador=0
  res=0
  for i in range(len(s)):

    if len(s)==1:
      res+=s[i]
    elif i==len(s)-1:
      continue
    else:
      for a in range(s[i],m):
        res=s[i]+s[i+1]
    
    if res==d:
      contador+=1

  return print(contador)"""



def solve(s, d, m):
    # Complete this function
    count = 0
    for i in range(0,len(s)):
        total = sum(s[i:m+i])
        if total == d:
            count+=1
    return print(count)


solve([1,2,1,3,2],3,2)

solve([4],4,1)

solve([2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1],18,7)