for _ in range(int(input())):
  n,total,i,primes=int(input()),1,0,[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
  while total<=n: total*=primes[i]; i+=1
  print(i-1)

#El arreglo estaria mejor declararlo afuera por la memoria pero asi se ven menos lineas
"""
Sample Input
6
1
2
3
500
5000
10000000000
Sample Output
0
1
1
4
5
10
"""