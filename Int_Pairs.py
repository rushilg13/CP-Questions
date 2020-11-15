# All Pairs of integer array whose sum is equal to target number
num=list(map(int, input().split()))
taregt=int(input())
ans=[]
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if(num[i]+num[j]==taregt):
            ans.append(num[i])
            ans.append(num[j])
            print(ans)
            ans=[]
