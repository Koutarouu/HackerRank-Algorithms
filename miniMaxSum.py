def miniMaxSum(arr):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    MaxSum=0
    MinSum=0
    for z in range(len(arr)):
      if z == 0:
        for i in range(len(arr)):
          if i==0:
            continue
          sum1+=arr[i]
      if z == 1:
          for i in range(len(arr)):
              if i==1:
                  continue
              sum2+=arr[i]
      if z == 2:
          for i in range(len(arr)):
              if i==2:
                  continue
              sum3+=arr[i]
      if z == 3:
          for i in range(len(arr)):
              if i==3:
                  continue
              sum4+=arr[i]
      if z == 4:
          for i in range(len(arr)):
            if i==4:
              continue
            sum5+=arr[i]

    if sum1 == sum2 == sum3 == sum4 == sum5:
      MaxSum=sum1
      MinSum=MaxSum

    if sum1>sum2 and sum1>sum3 and sum1>sum4 and sum1>sum5:
      MaxSum=sum1
    elif sum2>sum1 and sum2>sum3 and sum2>sum4 and sum2>sum5:
      MaxSum=sum2
    elif sum3>sum1 and sum3>sum2 and sum3>sum4 and sum3>sum5:
      MaxSum=sum3
    elif sum4>sum1 and sum4>sum2 and sum4>sum3 and sum4>sum5:
      MaxSum=sum4
    elif sum5>sum1 and sum5>sum2 and sum5>sum3 and sum5>sum4:
      MaxSum=sum5

    if sum1<sum2 and sum1<sum3 and sum1<sum4 and sum1<sum5:
      MinSum=sum1
    elif sum2<sum1 and sum2<sum3 and sum2<sum4 and sum2<sum5:
      MinSum=sum2
    elif sum3<sum1 and sum3<sum2 and sum3<sum4 and sum3<sum5:
      MinSum=sum3
    elif sum4<sum1 and sum4<sum2 and sum4<sum3 and sum4<sum5:
      MinSum=sum4
    elif sum5<sum1 and sum5<sum2 and sum5<sum3 and sum5<sum4:
      MinSum=sum5

    res="%d %d"%(MinSum,MaxSum)
    return res

print(miniMaxSum([5,5,5,5,5]))

#lst = map(int,str(input()).strip().split(' '))
#x = sum(lst)
#print (x-(max(lst))), (x-(min(lst)))