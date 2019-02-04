def designerPdfViewer(h, word):
  #print(min(h["abcdefghijklmnopqrstuvwxyz".index(a)] for a in word))
  return max(h["abcdefghijklmnopqrstuvwxyz".index(a)] for a in word) * len(word)


h = list(map(int, input().rstrip().split()))
word = input()
print(designerPdfViewer(h, word))