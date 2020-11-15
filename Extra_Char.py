# https://www.geeksforgeeks.org/find-one-extra-character-string/
# Find one extra character in a string
st1=str(input())
st2=str(input())
count=0
for i in st2:
    if(i not in st1):
        print(i)
    else:
        n1=str.count(st1,i)
        n2=str.count(st2,i)
        if(n2>n1):
            print(i)
            break
