def catAndMouse(x, y, z):
  catA=abs(z-x)
  catB=abs(z-y)
  if catA<catB:
    return "Cat A"
  elif catB<catA:
    return "Cat B"
  elif catB==catA:
    return "Mouse C"

q = int(input())
for q_itr in range(q):
  x,y,z = map(int,input().split())
  print(catAndMouse(x,y,z))


"""
2
1 2 3
1 3 2
Cat B
Mouse C
"""