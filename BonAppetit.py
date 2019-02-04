# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
  bcharged=sum(bill)/2
  bill.pop(k)
  bactual=sum(bill)/2
  #print(bactual)
  if b==bactual:
    return "Bon Appetit"
  else:
    return "%i"%(bcharged - bactual)

if __name__ == '__main__':
  nk = input().rstrip().split()

  n = int(nk[0])

  k = int(nk[1])

  bill = list(map(int, input().rstrip().split()))

  b = int(input().strip())

  print(bonAppetit(bill, k, b))

"""
si me da lo necesario ya le pago la diferencia despues de lo que debo haber pagado
4 1
3 10 2 9
7
Bon Appetit
bill
factura : una matriz de enteros que representa el costo de cada artículo pedido
k : un entero que representa el índice basado en cero del artículo que Anna no come
b : la cantidad de dinero que Anna contribuyó a la factura
"""
