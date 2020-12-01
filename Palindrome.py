# Approach 1
# def reverseDigits(num) :  
#     n = num
#     rev_num = 0;  
#     while (num > 0) : 
#         rev_num = rev_num * 10 + num % 10
#         num = num // 10
      
#     if n==rev_num:
#         return True
#     else:
#         return False  

# num = int(input())
# num = abs(num)
# print(reverseDigits(num))



# Approach 2
# num = int(input())
# num = abs(num)
# l1=[]
# while num > 0:
#     rem = num%10
#     l1.append(rem)
#     num = int(num/10)
# l2 = l1
# l1.reverse()
# if l1 == l2:
#     print("True")
# else:
#     print("False")



# Approach 3
# import math
# num = 2002
# l = int(math.log10(num)) +1   # Takes O(1) to calculate length
# if l%2==0:
#     l1=l2=[]
#     while num > 0:
#         rem = num%10
#         l1.append(rem)
#         num = int(num/10)
    
#     left = l1[:2]
#     right = l2[2:]
#     right.reverse()
#     if (left == right):
#         print("True")
#     else:
#         print("False")
    
# else:
#     l1=l2=[]
#     while num > 0:
#         rem = num%10
#         l1.append(rem)
#         num = int(num/10)
    
#     left = l1[:2]
#     right = l2[3:]
#     right.reverse()
#     if (left == right):
#         print("True")
#     else:
#         print("False")



# Approach 4 - Recursive
# def rev(n, temp):  
  
#     if (n == 0):  
#         return temp

#     temp = (temp * 10) + (n % 10)
#     return rev(n / 10, temp)
  
# n = int(input())
# temp = rev(n, 0)
  
# if (temp != n):  
#     print("True")  
# else: 
#     print("False") 



# Approach 5
# num = int(input())
# temp = num
# s=""
# while num>0:
#     rem = num % 10
#     s = s + str(rem)
#     num = int(num/10)
# if(temp == int(s)):   # or  if(str(temp) == s) ....
#     print("True")
# else:
#     print("False")


# Approach 6
num = str(input())
s = ""
for i in range(len(num)-1, -1, -1):
    s = s+num[i]
if (s==num):
    print("True")
else:
    print("False")