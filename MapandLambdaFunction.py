cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n<=2: return [i for i in range(n)]
    lis=[0]*n
    lis[0],lis[1]=0,1
    for i in range(2,n):
        lis[i]=lis[i-2]+lis[i-1]
    return lis

if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))

"""
print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has
only one line in its body. It proves very handy in functional and GUI programming.
sum = lambda a, b, c: a + b + c
sum(1, 2, 3)
6
Note:
Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function
and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.
"""