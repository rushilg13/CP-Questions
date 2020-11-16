# Check Rotations

'''
1. Create a temp string and store concatenation of str1 to
       str1 in temp.
        temp = str1.str1
        
2. If str2 is a substring of temp then str1 and str2 are 
       rotations of each other.
'''
st1=str(input())
st2=str(input())
st1=st1+st1
n=st1.count(st2)
if(n>0):
    print("They are Rotations")
else:
    print("They are not Rotations")