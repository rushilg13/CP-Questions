# Remove Punctuations
# https://www.geeksforgeeks.org/removing-punctuations-given-string/
st=str(input())
count=0
for i in '''!"#$%&'()*+,-./:;?@[\]^_`{|}~<>''':
    if(i in st):
        st=st.replace(i,'')
print(st)

    