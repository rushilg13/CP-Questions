# https://www.codechef.com/problems/LECANDY

test=int(input())
count=1
tot=0
ans=[]
while(count<=test):
    count=count+1
    ne_nc=list(map(int, input().split(' '))) 
    ele=ne_nc[0]
    can=ne_nc[1]
    need=list(map(int, input().split(' '))) 
    for i in range(ele):
        tot=tot+need[i]
    if(tot<=can):
        ans.append("Yes")
    else:
        ans.append("No")
for i in ans:
    print(i)
        
    
    