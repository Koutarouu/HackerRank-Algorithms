from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
  res=0
  dar=Counter(ar)
  for k,v in dar.items():
    res+=v//2
  return res

if __name__ == '__main__':

  n = int(input())

  ar = list(map(int, input().rstrip().split()))

  result = sockMerchant(n, ar)
  print(result)

###El programa cuenta lso pares de calcetines disponibles
"""
Input(stdin)
9
10 20 20 10 10 30 50 10 20
"""