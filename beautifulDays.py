def beautifulDays(i, j, k):
  contador=0
        #int(x)
  lista=[str(x) for x in range(i,j+1)]
  for i in lista:
      #abs(i-int(str(i)[::-1]))
    if abs(int(i)-int(i[::-1]))%k==0:
      contador+=1
  return contador

#i, j, k = [int(x) for x in input().split()]


i,j,k = map(int,input().split())
print(beautifulDays(i, j, k))
              #importante este uno lo usaremos como contador si le pusiera como en el de arriba day for day me sumaria 20 + 22 aqui el valor de uno no cambia
beautifulDays = [1 for day in range(i, j+1) if (day - int(str(day)[::-1])) % k == 0]
print(beautifulDays,sum(beautifulDays))
#print(sum((int(abs(day - int(str(day)[::-1])) % k == 0) for day in range(i,j+1))))
"""
Datos de entrada
13 45 3 y 20 23 6
Salidas
33 y 2
"""