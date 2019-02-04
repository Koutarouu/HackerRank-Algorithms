def plusMinus(arr):
    n=len(arr)
    positives=0
    negatives=0
    zeros=0
    for i in range(len(arr)):
        if arr[i] > 0:
            positives+=1
        elif arr[i]<0:
            negatives+=1
        else:
            zeros+=1
    positives=format(positives /n ,'.6f')
    negatives=format(negatives /n,'.6f')
    zeros=format(zeros /n,'.6f')
    #res= str(positives)+" "+str(negatives)+" "+str(zeros)
    return print(positives) , print(negatives) , print(zeros)

plusMinus([1,2,3,-4,0,0])