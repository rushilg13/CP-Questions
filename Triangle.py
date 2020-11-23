# Find Number of triangles possible with sides given in arr

n=3
count=0 
arr= [3,4,5]
arr.sort()
for i in range(n-1):
    for j in range(0,n+1):
        j=arr[n-j-1:n-j]
        for k in j:
            if(arr[i]+arr[i+1]>=k) and arr[i]!=arr[i+1] and arr[i]!=k and arr[i+1]!=k:
                # print(arr[i],arr[i+1],k)
                count+=1
if count%2==0:
    count=count/2
else:
    count=count-((count-1)/2)
print((int)(count))

