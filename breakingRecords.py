def breakingRecords(scores):
  low=0
  great=0
  recordl=scores[0]
  recordg=scores[0]
  for i in range(len(scores)):
    if scores[i]>recordg:
      great+=1
      recordg=scores[i]
    elif scores[i]<recordl:
      low+=1
      recordl=scores[i]
    
  return print(great), print(low)


breakingRecords([10,5,20,20,4,5,2,25,1])
breakingRecords([3,4,21,36,10,28,35,5,24,42])
