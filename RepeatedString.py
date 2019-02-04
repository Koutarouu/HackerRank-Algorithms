import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
  lol=0
  lon=len(s)
  l=n//lon
  ll=n/lon
  if l==ll:
    s=list(filter(lambda x: x=='a', s))
    return (len(s)*l)
  else:
    for i in range(0,(n-(l*lon))):
      lol+=(1 if s[i]=='a' else 0)
    s=list(filter(lambda x: x=='a', s))
    return (len(s)*l)+lol
  return 0

if __name__=='__main__':
  s=input()
  n=int(input())
  result=repeatedString(s, n)
  print(result)

"""
Sample Input 0
aba
10
Sample Output 0
7
"""