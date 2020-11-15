# https://www.geeksforgeeks.org/check-whether-number-duck-number-not/
# Duck Number
st=str(input())
for i in range(1,len(st)):
    if(st[i]=='0'):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Duck number")
else:
    print("Not a duck number")



    