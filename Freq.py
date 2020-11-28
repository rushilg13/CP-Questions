# Microsoft Question
# Given an array find the Majority element in the array (an element whose frequency in that array is strictly greater than half of the size of the array.) and if there is no majority return -1.
# O(N)

def major(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    print(freq) # For Debugging
    keys = list(freq.keys())
    values = list(freq.values())
    maxi = max(values)
    if (maxi > (len(arr)/2)):
        print (keys[(values.index(maxi))])
    else:
        return -1

nums = list(map(int, input().split()))
major(nums)