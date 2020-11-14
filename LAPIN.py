# https://www.codechef.com/problems/LAPIN
test=int(input())
count=1
flag=0
while(count<=test):
    count=count+1
    st=str(input())
    leng=len(st)
    if(leng%2!=0):
        ind=int(leng/2)
        half1=st[:ind]
        half2=st[ind+1:]
    else:
        ind=int((leng/2))
        half1=st[:ind]
        half2=st[ind:]
    for i in half1:
        count1=str.count(half1,i) 
        count2=str.count(half2,i)
        if(count1==count2):
            flag=flag+1
    if(flag==len(half1)):
        print("YES")
        flag=0
    else:
        print("NO")
        flag=0
