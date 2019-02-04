from collections import Counter

"""def migratoryBirds(ar):
  tupla=(1,2,3,4,5)
  con1=0
  con2=0
  con3=0
  con4=0
  con5=0
  for i in range(len(ar)):
    if ar[i] == tupla[0]:
      con1+=1
    elif ar[i] == tupla[1]:
      con2+=1
    elif ar[i] == tupla[2]:
      con3+=1
    elif ar[i] == tupla[3]:
      con4+=1
    elif ar[i] == tupla[4]:
      con5+=1

  mF= max(con1,con2,con3,con4,con5)
  if mF==con1:
    return ar[0]
  elif mF==con2:
    return ar[1]
  elif mF==con3:
    return ar[2]
  elif mF==con4:
    return ar[3]
  elif mF==con5:
    return ar[4]

print(migratoryBirds([1,4,4,4,5,3]))"""
def migratoryBirds(ar):
  arr=[1,2,3,4,5]
  mF=Counter(ar).most_common()[0][0]
  if mF==arr[0]:
    return 1
  elif mF==arr[1]:
    return 2
  elif mF==arr[2]:
    return 3
  elif mF==arr[3]:
    return 4
  elif mF==arr[4]:
    return 5
  

print(migratoryBirds([1,4,4,4,5,3]))