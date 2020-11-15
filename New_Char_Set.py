# https://www.geeksforgeeks.org/change-string-to-a-new-character-set/

char=str(input())
cha=[]
alpha="a b c d e f g h i j k l m n o p q r s t u v w x y z"
for i in char:
    cha.append(i)
alpha=alpha.split(' ')
dic=dict(zip(cha,alpha))
st=str(input())
for i in st:
    print(dic[i],end='')