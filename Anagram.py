# Check Anagram
st1=str(input())
st2=str(input())
flag=0
for i in st1:
    if(str.count(st1,i)==str.count(st2,i)):
        flag+=1
if(flag==len(st1)):
    print("Anagram")
else:
    print("Not Anagram")



