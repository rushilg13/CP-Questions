# Check Pangram
# https://www.geeksforgeeks.org/pangram-checking/
st=str(input())
for i in 'qwertyuiopasdfghjklzxcvbnm':
    if(i in st):
        flag=1
    else:
        print("Not Pangram")
        break
if(flag==1):
    print("Pangram")
    