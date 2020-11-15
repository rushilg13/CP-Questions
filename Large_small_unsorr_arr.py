# Largest and Smallest number in unsorted array
num=list(map(int, input().split()))
maxi=num[0]
mini=num[0]
for i in range(1,len(num)-1):
    if mini>num[i]:
        mini=num[i]
    elif maxi<num[i]:
        maxi=num[i]
print(mini)
print(maxi)