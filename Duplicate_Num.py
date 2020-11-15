# Duplicate number in an array
# Approach 1 - Sum of numbers - Time complexity= O(n) space complexity= O(1)
# If array contains consecutive numbers
num=list(map(int, input().split()))
sum=0
for i in num:
    sum=sum+i
print(int(sum-(((len(num)-1)*(len(num)))/2)))

# Duplicate number in an array
# Approach 2 - Sum of numbers
# If numbers are not consecutive
num=list(map(int, input().split()))
sum1=0
sum2=0
num_set=list(set(num))
for i in num:
    sum1=sum1+i
for i in num_set:
    sum2=sum2+i
print(sum1-sum2)



    



    
