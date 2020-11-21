# Find number of perf sq in a range taken by user
n1=int(input())
n2=int(input())
count=0
for i in range(n1,n2+1):
    if((int(i**0.5))==int((i**0.5)**2)**0.5):
        count+=1
print(count)
