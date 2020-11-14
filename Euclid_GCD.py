# Euclid-GCD
print("Enter number 1: ")
n1=int(input())
print("Enter number 2: ")
n2=int(input())
if(n1>n2):
    dividend=n1
    divisor=n2
else:
    dividend=n2
    divisor=n1
while(divisor!=0):
    remainder=dividend % divisor
    dividend=divisor
    divisor=remainder
print(dividend)