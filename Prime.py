# O(sqrt(n)) algorithm for finding whether a number is a prime
print("enter a number to check if prime or not")
num=int(input())
for i in range(2,int((num**0.5)+1)):
    if(num%i==0):
        flag=0
        break
    else:
        flag=1

if(flag==1):
    print("Prime")
else:
    print("Composite")