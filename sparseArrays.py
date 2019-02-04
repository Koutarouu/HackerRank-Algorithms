def matchingStrings(strings, queries):
  new=[]
  for i in range(len(queries)):
    contador=0
    for j in range(len(strings)):
      
      if strings[j] == queries[i]:
        contador+=1
    new.append(contador)

  return new
        

    

print(matchingStrings(["aba","baba","aba","xzxb"],["aba","xzxb","ab"]))