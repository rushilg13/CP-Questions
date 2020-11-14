# https://www.codechef.com/problems/CSUB
test=int(input())
count=1

while(count<=test):
    count=count+1
    leng=int(input())
    bi=str(input())
    n=str.count(bi,'1')
    total=int(n*(n+1)/2)
    if(n==1):
        ans=1
    elif(n==2):
        ans=3
    else:
        ans=int(total)
    print(total)

    