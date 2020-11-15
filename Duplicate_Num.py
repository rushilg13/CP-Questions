# Duplicate number in an array form 1 to 10

# Approach Sum of numbers - Time complexity= O(n) space complexity= O(1)
num=list(map(int, input().split()))
sum=0
for i in num:
    sum=sum+i
print(int(sum-(((len(num)-1)*(len(num)))/2)))



    