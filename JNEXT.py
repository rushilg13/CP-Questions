# https://www.spoj.com/problems/JNEXT/

# INCOMPLETE!!!!
test=int(input())
count=1

while(count<=test):
    dum=[]
    count=count+1
    digi=int(input())
    num=list(map(int, input().split()))
    num.reverse()
    for i in range (digi-1):
        if num[i]>num[i+1]:
            for j in range(0,i+1):
                dum.append(num[j])
                    
            mini=min(dum)
            ind=num.index(mini)
            dum=[]
            temp=num[i+1]
            num[i+1]=mini
            num[ind]=temp
            # for j in range(0,ind):
            #     dum.append(j)
            # dum.sort()
            # num.reverse()
            for j in range(0, i+1):
                dum.append(num[j])
            dum.sort()
            num=num[i+1:]
            print(num)
            print(dum)
            num.reverse()
            num=num+dum
            for i in num:
                print(i,end="")
            break













