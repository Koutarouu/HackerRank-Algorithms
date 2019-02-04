n,k=map(int,input().split())
r_q,c_q=map(int,input().split())
obstacles=[]
for _ in range(k):
	obstacles.append(list(map(int,input().split())))
u = n-r_q # North
s = r_q-1 # South
e = n-c_q # East
o = c_q-1 # West
en,es,on,os = min(u,e),min(s,e),min(u,o),min(s,o)
for i in obstacles:
	if i[0]==r_q and i[1]<c_q: o=min(o,c_q-1-i[1])
	elif i[0]==r_q and i[1]>c_q: e=min(e,i[1]-c_q-1)
	elif i[1]==c_q and i[0]>r_q: u=min(u,i[0]-r_q-1)
	elif i[1]==c_q and i[0]<r_q: s=min(u,r_q-1-i[0])
	elif abs(i[0]-r_q)==abs(i[1]-c_q): #si el obstaculo esta en diagonal
		if i[1]>c_q:
			if i[0]>r_q: en=min(en,i[1]-c_q-1)
			else: es=min(es,i[1]-c_q-1)
		else:
			if i[0]>r_q: on=min(on,c_q-1-i[1])
			else: os=min(os,c_q-1-i[1])
print(s+u+o+e+en+es+on+os) #la suma de todos los lados menos los obstaculos

"""for i in obstacles:
	if i[1] == c_q: # si la columna del obstaculo y la columna de la reina son las mismas
		if i[0] < r_q: #Si la fila del obstaculo es menor que la de la reina
			s=min(s, r_q-1-i[0]) #s toma el valor menor entre el sur y el mismo sur original menos la columna del obstaculo
		else: #si esta en la parte de arriba de la reina
			u=min(u, i[0]-r_q-1) #n toma el valor menor entre el norte y la fila del obstaculo menor menos el sur original
	elif i[0] == r_q: #si estan en la misma fila
		if i[1] < c_q: #si el obstaculo esta a la izquierda de la reina
			o = min(o, c_q-1-i[1]) #o toma el valor menor entre el oeste y todo el oeste original menor la columna del obstaculo
		else: #si el obstaculo esta a la derecha de la reina
			e = min(e, i[1]-c_q-1) #e toma  el valor menor entre el este y la columna del obstaculo menos la columna de la reina menos 1
	elif abs(i[0]-r_q) == abs(i[1]-c_q): #Si el valor absoluto de la fila del obstaculo menos la fila de la reina es igual al valor absoluto de la columna del obstaculo menos la columna de la reina
		if i[1]>c_q: #si el obstaculo esta a la derecha
			if i[0]>r_q: #si el obstaculo esta arriba de la reina
				en= min(en, i[1]-c_q-1) #arriba a la derecha toma el valor menor entre en y la columna del obstaculo menos la columna de la reina menos 1
			else: #a la derecha abajo
				es= min(es, i[1]-c_q-1)
		else: #si esta a la izquierda
			if i[0]>r_q: #ariba a la izquierda
				on=min(on, c_q-1-i[1]) #on toma el valor menor entre on y la de todos los obstaculos a la derecha de la reina menos la columna del obstaculo
			else: #abajo ala izquierda
				os=min(os, c_q-1-i[1])
"""
"""
No cree la cuadrícula. Piensa matemáticamente. Cada una de las líneas diagonales debe tener una pendiente de 1 o -1. Las líneas horizontales requieren que el valor y sea el mismo y las líneas verticales
requieren que el valor x sea el mismo. Entonces, todo lo que se necesita es hacer un seguimiento de los obstáculos que están en el eje horizontal o vertical de la reina o que tienen una diagonal con una
pendiente de -1 o 1. Entonces, si el valor absoluto de | x_q - x_o | = | y_q - y_o | (donde * _q representa los puntos para la reina y * _o representa los puntos para el obstáculo) la reina se encontrará
con el obstáculo en la línea diagonal. Por lo tanto, mantenga ocho variables mínimas, cada una representando la dirección a la que puede ir la reina. Inicialice cada una de las ocho variables con la
posición de la reina en el borde del tablero. A continuación, compara cada uno de los obstáculos para ver si se encuentra en el camino de la reina. Si se encuentra en el camino, calcule la distancia desde
la reina hasta el obstáculo y si la distancia es menor que la distancia mínima para esa dirección, entonces reemplace la distancia mínima con la nueva distancia. Si la distancia mínima para una dirección
es cero, entonces puede ignorar cualquier obstáculo en esa dirección. Una vez que hayas analizado los obstáculos, simplemente suma las distancias
"""