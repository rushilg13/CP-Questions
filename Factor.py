# Factor of n

n=int(input())
factors=[]
for i in range(2,int((n**0.5)+1)):
    if(n%i==0):
        factors.append(i)
        factors.append(int(n/i))

print(set(factors))
