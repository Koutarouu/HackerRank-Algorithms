def utopianTree(n):
  new=[]
  cont=0
  for i in range(n+1):
    if i%2!=0:
      cont*=2
      new.append(cont)
    else:
      cont+=1
      new.append(cont)
  return new[n]


t = int(input())
for t_itr in range(t):
  n = int(input())
  print(utopianTree(n))


"""
El arbol utopiano crece en primavera lo que media por 2 y en verano solo un metro
el arbol inicia midiendo un metro pero eso se lo asigno con el primer cont+=1
Sample Input
3
0
1
4
Output
1
2
7

"""