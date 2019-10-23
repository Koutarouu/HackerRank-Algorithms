# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p:int, q:int) -> list:
    def iskaprekar(item: int):
        if item == 1: return True 
        d=len(str(item))
        sItem = str(item**2)
        le=len(sItem)
        if le == 1: return False
        l = int(sItem[:d] if le%2==0 else sItem[:d-1])
        r = int(sItem[d:] if le%2==0 else sItem[d-1:])
        return (l+r)==item

    res=[]
    for i in range(p, q+1):
        if iskaprekar(i):
            res.append(i)
    if res:
        print(*res)
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    kaprekarNumbers(p, q)
