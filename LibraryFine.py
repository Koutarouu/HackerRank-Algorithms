d1,m1,y1=map(int,input().split())
d2,m2,y2=map(int,input().split())
fine=0
if y1>y2:
  fine=10000
if y1==y2:
  if m1>m2:
    fine=(m1-m2)*500
  if m1==m2 and d1>d2:
    fine=(d1-d2)*15
print(fine)

"""if (d1<=d2 and m1<=m2 and y1<=y2) or (m1<m2 and y1<=y2) or y1<y2:
  fine=0
else:
  if d1>d2 and m1<=m2 and y1<=y2:
    fine+=(d1-d2)*15
  elif d1<=d2 and m1>m2 and y1<=y2:
    fine+=(m1-m2)*500
  elif d1<=d2 and m1<=m2 and y1>y2:
    fine+=(y1-y2)*10000
  elif d1>d2 and m1>m2 and y1<=y2:
    fine+=(m1-m2)*500
  elif d1>d2 and m1<=m2 and y1>y2:
    fine+=(y1-y2)*10000
  elif d1<=d2 and m1>m2 and y1>y2:
    fine+=(y1-y2)*10000
  else:
    fine+=(y1-y2)*10000
"""
