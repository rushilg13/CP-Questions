
# Write a prog that makes the first number as large as possible by swapping out its digits for each digit in second number. Each digit in 2nd number can only be used once.
# Test Cases
# 523. 76  -> 763
# 9132, 5564  -> 9655
# 8732, 91255  -> 9755

num1 = str(input())
num2 = str(input())
l1=[]
l2=[]
for i in num1:
    l1.append(int(i))
for i in num2:
    l2.append(int(i))
l2.sort()
l2.reverse()
print(l1,l2)
for i in range(len(l1)):
    if(len(l2) != 0):
        if(l1[i]<l2[0]):
            l1[i]=l2[0]
            del l2[0]
        else:
            continue
    else:
        break
print(l1)


