from functools import reduce
from math import factorial

def extraLongFactorials(n):
  res=1
  for i in range(1,n+1):
      res*=i
  print(res)

def fact(n):
  if n==1:
    return 1
  prod=n*fact(n-1)
  return prod

def get_factorial2(n):
  old = [1]
  current = []
  for i in range(2, n+1):
    carry = 0
    for digit in old:
      prod = int(digit) * i + carry
      rem = prod % 10
      current.append(rem)
      carry = prod // 10
    if carry != 0:
      for j in str(carry)[::-1]:
        current.append(j)  # add j as a str
    old = current
    current = []
  
  return "".join(map(str,old[::-1])) # convert everything to str before concatenation and returning the results
              
          

print(get_factorial2(25))

#n = int(input())
extraLongFactorials(25)
print(fact(25))
print(reduce(lambda x, y: x*y, range(25+1)[1:]))
print(factorial(25))
