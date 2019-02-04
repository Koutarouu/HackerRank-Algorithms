from bisect import bisect_right


def climbingLeaderboard(scores, alice):
  scores=sorted(list(set(scores)),reverse=True)
  alice=sorted(alice)
  new=[]
  l=len(scores)
  for i in alice:
    while l>0 and i>=scores[l-1]:
      l-=1
    print(l+1)

def climbingLeaderboard2(scores, alice):
  scores=sorted(list(set(scores)))
  alice=sorted(alice)
  for i in alice:
    print(bisect_right(scores,i))
    print(len(scores)-bisect_right(scores,i)+1)

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
climbingLeaderboard(scores, alice)
print("==========================================================")
climbingLeaderboard2(scores, alice)