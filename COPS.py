# https://www.codechef.com/problems/COPS
test=int(input())
count=1
l1=[]
res=[]

while(count<=test):
    count=count+1
    for i in range(1,101):
        l1.append(i)
        comp=set(l1)
    l1=[]
    m_x_y=list(map(int, input().split()))
    m=m_x_y[0]
    x=m_x_y[1]
    y=m_x_y[2]
    houses=list(map(int, input().split()))
    search=x*y
    for i in range(m):
        #if(houses[i]<=search):
        for j in range(houses[i], houses[i]-search-1, -1):
            l1.append(j)
        l1=set(l1)
        comp=comp-l1
        
        l1=[]
        for j in range(houses[i], houses[i]+search+1):
            l1.append(j)
        l1=set(l1)
        comp=comp-l1
        l1=[]
    #print(comp)
    ans=len(comp)
    print(ans)
