from collections import Counter
m,n=map(int,input().split())
attendes=[]
c,w=0,0
new=[]
s={}
for _ in range(m):
  attendes.append(input()) 
for o in attendes:    
  i=0
  ch={}
  for j in o:
    if w<n:
      s[str(w)]=1
    ch[str(i)]=int(j)
    i+=1
    w+=1
  new.append(ch)
s=Counter(s)
temp=s
kt=0 # known Topics
ctemp=len(temp)
for t in range(len(new)):
  for y in range(t+1,len(new)):
    s=temp
    s=s-Counter(new[t])
    s=s-Counter(new[y])
    ty=kt
    kt=(ctemp-len(s)) if (ctemp-len(s))>kt else kt
    if ty!=kt:
      c=0
    c+=1 if (ctemp-kt)==len(s) else 0
print(kt,c,sep='\n')
