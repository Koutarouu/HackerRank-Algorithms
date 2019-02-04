"""def gradingStudents(grades):
  n=len(grades)
  new=0
  new2=[]
  base=5
  for i in range(len(grades)):
    a=(100-grades[i])%5

    new=grades[i]+a
    if new<40:
      new=grades[i]
    elif new-grades[i]<3:
      new=new
    elif new-grades[i]==3:
      new=grades[i]
    new2.append(new)
  return new2
      

print(gradingStudents([73,67,38,33]))"""
def gradingStudents(grades):
  new2=[]
  for i in range(len(grades)):
    if grades[i] < 38 or grades[i] % 5 < 3:
      grades[i]=grades[i]
    else:
      grades[i]=grades[i] + (5 - (grades[i] % 5))
    new2.append(grades[i])
  return new2

print(gradingStudents([73,67,38,33]))
#print(int(base*round(float(grades[i])/base)))
"""

consider 51 need to converted to 55

 code here

mark=51;
r=100-mark;
a=r%5;
new_mark=mark+a;
"""