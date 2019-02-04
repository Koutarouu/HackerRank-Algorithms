if __name__ == '__main__':
    n = int(input())
    
    def fun(n):
        total = []
        for i in range(1,n+1):
            total.append(i)
        return total

    print(*fun(n),sep='')
    print(fun(n))