# Complete the countingValleys function below.
def countingValleys(n, s):
  niveldelmar=0
  contador=0
  valleys=0
  for i in range(niveldelmar,len(s)):
    if s[i]=="U":
      contador+=1
    elif s[i]=="D":
      contador-=1
    if contador==niveldelmar and s[i]=="U":
      valleys+=1
  return valleys


print(countingValleys(8,"UDDDUDUU"))
print(countingValleys(12,"DDUUDDUDUUUD"))
print(countingValleys(10,"DDUDDUUDUU"))