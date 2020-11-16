# Maximum and minimum sums from two numbers with digit replacements
# https://www.geeksforgeeks.org/maximum-minimum-sums-two-numbers-digit-replacements/

def mini(st1,st2):
    for i in st1:
        if(i=='6'):
            st1=st1.replace(i,'5')
    for i in st2:
        if(i=='6'):
            st2=st2.replace(i,'5')

    st1=int(st1)
    st2=int(st2)
    print("Minimum is: ", st1+st2)



def maxi(st1,st2):
    for i in st1:
        if(i=='5'):
            st1=st1.replace(i,'6')
    for i in st2:
        if(i=='5'):
            st2=st2.replace(i,'6')

    st1=int(st1)
    st2=int(st2)
    print("Maximum is: ", st1+st2)

st1=str(input())
st2=str(input())
mini(st1,st2)
maxi(st1,st2)
