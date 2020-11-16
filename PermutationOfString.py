# Find all permutations of the string ie Substring

st1 = str(input())
ans=[]
for i in range (len(st1)):
    for j in range(i,len(st1)):
        ans.append(st1[i:j])
        ans.append(st1[i:])

print(set(ans)-{''})
print(len(set(ans)-{''}))