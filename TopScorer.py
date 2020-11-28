# Microsoft Question
# Find the sum of the top K scores in a competition.
# O(K)
def topScorer(arr, k):
    arr.sort()
    arr.reverse()
    arr = arr[:k]
    print(arr)
    sumi = 0
    for i in arr:
        print(i)
        sumi = sumi + i
    print(sumi)


marks = list(map(int,input().split()))
k = int(input())
topScorer(marks, k)