from collections import Counter

"""def birthdayCakeCandles(ar):
  #n=len(ar)
  contador=0
  for i in range(len(ar)):

    if ar[i]==max(ar):
      contador+=1
  return contador
    """
def birthdayCakeCandles(ar):
    d = Counter(ar)
    largest_key = max(Counter.keys(d))
    return d.get(largest_key)

#print(birthdayCakeCandles([3,2,3,1]))
print(birthdayCakeCandles([3,2,3,1]))