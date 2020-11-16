# Count Vowels
st1=str(input())
v=0
for i in st1:
    if(i in 'aeiouAEIOU'):
        v+=1
print("Number of vowels are: ", v)
print("Number of consonants are: ", len(st1)-v)

    