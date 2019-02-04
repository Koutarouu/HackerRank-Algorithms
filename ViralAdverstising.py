def viralAdvertising(n):
  comulative=0
  people=5
  for i in range(n):
    people=people//2
    comulative+=people
    people*=3
  return (people,comulative)
#Me falto analizar el problema mas para llegar ala conclusion de que tenia que multiplicarlos por 3
n = int(input())
print(viralAdvertising(n))

m = [2]
for i in range(n-1):
  m.append(3*m[i]//2)
print(sum(m))
print(m)
#este de arriba es el mas facil de entender
total = 2;
liked = 2;
for _ in range(n-1):
  liked = liked * 3//2
  total += liked
print(total)


m = 2
tot = 2
for _ in range(1,n):
  m += m>>1
  tot += m
print(tot)

"""
Here's how it works:

floor(3x / 2)
floor(2x/2 + x/2)
floor(x + x/2)
x + floor(x/2) --->{since x is int, see here}
x + x>>1 -------->{bitwise shift right x by k = floor(x/2^k}
Method taken from here
"""