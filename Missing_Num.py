# Missing number in an array form 1 to 10

# Approach 1 Will work even if unsorted
num=list(map(int, input().split()))
for i in range(1,11):
    if(i not in num):
        print(i)

# Approach 2 Needs Sorted array
num=list(map(int, input().split()))
for i in range(0,10):
    if(num[i+1]!=num[i]+1):
        print(num[i])

   

# Approach 3 first sort then use approach 2
num=list(map(int, input().split()))
num.sort()
for i in range(0,10):
    if(num[i+1]!=num[i]+1):
        print(num[i])

# Approach 4 BEST ONE!   Time complexity= O(n) space complexity= O(1)
num=list(map(int, input().split()))
sum=0
for i in num:
    sum=sum+i
print(int((((len(num)+1)*(len(num)+2))/2)-sum))



    