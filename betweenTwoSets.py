from fractions import gcd

def getTotalX(a, b):
  contador=0
  for i in range(len(b)):
    #if len(a)==1 and len(b)==1:
      #contador=9
    if len(a)==1 and a[0]%2==0:
      contador=1
    elif b[i]%a[i-1]==0:
      contador+=1
    else:
      continue
  return contador

#print(getTotalX([2,4],[16,32,96]))


print(getTotalX([2],[20,30,12]))

def getTotalX(a, b):
    lcm_num = a[0]
    gcd_num = b[0]
    if len(a) > 1:
        for x in range(1,len(a)):
            lcm_num =  (lcm_num * a[x])/gcd(lcm_num,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gcd_num = gcd(gcd_num,b[x])
    count = 0
    for x in range(int(lcm_num), gcd_num+1, int(lcm_num)):
        if gcd(x, gcd_num) == x:
            count += 1
    return count

print(getTotalX([2,4],[16,32,96]))