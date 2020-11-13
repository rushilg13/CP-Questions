# https://www.codechef.com/problems/CNOTE
test = int(input())
count=1
ans=[]
flag=0
while(count<=test):
    count=count+1
    nums=list(map(int, input().split()))
    x=nums[0]
    y=nums[1]
    k=nums[2]
    n=nums[3]
    for i in range (n):
        if(flag==0):
            pc=list(map(int, input().split()))
            p=pc[0]
            c=pc[1]
            flag=0
            if(k>=c and x<=y+p):
                flag=1
            else:
                flag=0
        else:
            pc=list(map(int, input().split()))
    if((flag==1)):
        ans.append("LuckyChef")
        flag=0
    elif((flag==0)):
        ans.append("UnluckyChef")
        flag=0
for i in ans:
    print(i)