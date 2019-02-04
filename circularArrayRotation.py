from collections import deque
"""
if __name__ == '__main__':
  n,k,q = map(int,input().split())
  a = list(map(int, input().rstrip().split()))
  a=a[-k:]+a[:-k]
  for _ in range(q):
    print(a[int(input())])
"""
if __name__ == '__main__':
  N, K, Q = list(map(int, input().split()))
  A = list(map(int, input().split()))
  for _ in range(Q):
    x = int(input())
    print(A[(x - K) % N])

if __name__ == '__main__':
  n,k,q = map(int,input().split())
  a = list(map(int, input().rstrip().split()))
  for _ in range(q):
      print(a[(int(input())-k)%n])
"""
n,k,q = map(int,input().split())
a = deque(map(int, input().rstrip().split()))
queries = []
a.rotate(k)
list(a)
for _ in range(q):
  print(a[int(input())])
"""
#print(circularArrayRotation(a, k, queries))