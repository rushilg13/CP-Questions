# Find misisng Pangram
# https://www.geeksforgeeks.org/missing-characters-make-string-pangram/
st=str(input())
for i in 'qwertyuiopasdfghjklzxcvbnm':
    if(i in st):
        flag=1
    else:
        print(i, end="")

    