# https://www.codechef.com/problems/SALARY

test=int(input())
count=1
counter=0
flag=0
ans=[]
while(count<=test):
    count=count+1
    num=int(input())
    work=list(map(int, input().split()))
    while(flag==0):
        mini=max(work)
        ind=work.index(mini)
        if(len(set(work))!=1):
            counter=counter+1
            for i in range(num):
                if(i!=ind):
                    work[i]=work[i]+1
                else:
                    continue
        else:
            flag=1
    ans.append(counter)
    counter=0
    flag=0
for i in ans:
    print(i)
    
    