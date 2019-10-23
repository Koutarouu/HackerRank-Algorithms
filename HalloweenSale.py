def howManyGames(p, d, m, s) -> int:
    # Return the number of games you can buy
    games=0
    while s-p>=0:
    	games+=1
    	s-=p
    	p=p-d if p-d>m else m
    return games

p,d,m,s=map(int,input().split())
print(howManyGames(p,d,m,s))