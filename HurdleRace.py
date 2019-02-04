def hurdleRace(k, height):
  if k>=max(height):
    return 0
  else:
    nax=max(height)-k
    return nax
  print(max(max(height)-k,0))
  #print(max(height) - k if max(height) > k else 0)

  #return k,height

n,k = map(int, input().split())
height = list(map(int, input().rstrip().split()))
print(hurdleRace(k, height))

"""Cuantas unidades de pocion tengo que consumir para pasar los
obstaculos
5 4
1 6 3 5 2


La fraseología es inequívoca, dice que "cada vez que Dan bebe una bebida mágica, la altura máxima que puede saltar durante la carrera aumenta por unidad"

Cada trago dura toda la carrera, por lo que está en lo cierto, solo necesita calcular la diferencia entre el obstáculo más alto y su máximo actual.
"""