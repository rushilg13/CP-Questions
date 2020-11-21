# Rain Trapping problem
arr = list(map(int, input().split()))
water=0
for i in range(1,len(arr)-1):
    left=arr[:i]
    right=arr[i+1:]
    ml=max(left)
    mr=max(right)
    maxi=max([ml,mr])
    water=water+(maxi-arr[i])

print("Units of water trapped is:",water)