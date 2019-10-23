def btwise(n: int, k: int):
    result = 0
    if n==2:
        return 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if k>(i&j)>result:
                result = (i&j)
            if (i&j)>k:
                return result
    return result


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(btwise(n, k))