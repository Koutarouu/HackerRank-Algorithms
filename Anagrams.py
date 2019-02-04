"""def makeAnagram(a, b):
  contador=0
  totalLen=len(a)+len(b)
  new=[]
  for i in range(len(a)):
    
    for j in range(len(b)):
      if contador>1:
        continue
      elif a[i]==b[j]:
        new.append(a[i])
        contador+=1

        

  return new
      """

def makeAnagram(a, b):
  count = 0
  for i in range(97, 123):
    ia = sum(letter == chr(i) for letter in a)
    ib = sum(letter == chr(i) for letter in b)
    count += abs(ia-ib)
    print(count)
  return count

print(makeAnagram("cde","abc"))
#print(makeAnagram("cde","dcfeafbcddc"))

#for i in range(97, 127):
  #print(chr(i))
  