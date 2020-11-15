# Check Pangram
# https://www.geeksforgeeks.org/pangram-checking/
st=str(input())
for i in 'qwertyuiopasdfghjklzxcvbnm':
    if(i in st):
        flag=1
    else:
        flag=0
        break
if(flag==1):
    print("Pangram")
else:
    print("Not Pangram")
    
