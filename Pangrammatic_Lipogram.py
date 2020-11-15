# Pangrammatic Lipogram
# https://www.geeksforgeeks.org/check-string-pangrammatic-lipogram/
st=str(input())
count=0
for i in 'qwertyuiopasdfghjklzxcvbnm':
    if(i in st):
        flag=1
    else:
        count=count+1
if count==1:
    print("Pangram Lipogram")
elif count==0:
    print("Pangram")
else:
    print("lipogram")

    