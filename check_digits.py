# Check if All Digits

st1 = str(input())
flag = 0
for i in st1:
    if(i.isdigit()==True):
        flag+=1
if(flag==len(st1)):
    print("All Digits")
else:
    print("Not All Digits")