def diagonalDifference(arr):
  con1=0
  con2=0
  difference=0
  con1= arr[0][0] + arr[1][1] + arr[2][2]
  con2= arr[0][2] + arr[1][1] + arr[2][0]
  difference=abs(con1-con2)
  return difference


print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))


def diagonalDifference(arr):
  con1=0
  con2=0
  difference=0
  for i in range(len(arr)):
    con1+=arr[i][i]
    con2+=arr[i][-i-1]
  difference=abs(con1-con2)
  return difference


print(diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]]))


#print(diagonalDifference([[11,2,4],[10,8,-12]]))
