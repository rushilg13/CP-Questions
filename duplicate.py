# find all duplicates
nums=str(input())
num_set=set(nums)
for i in num_set:
    count=str.count(nums,i)
    if(count>1):
        print(i)
