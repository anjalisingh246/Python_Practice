# 1
#  n = int(input("enter the number: "))
# rev,x = 0,n

# while n > 0:
#     ld = n%10
#     rev = rev*10+ld
#     n = n//10  
# if rev==x:
#       print(f'number {x} is palindrome') 
# else:
#      print(f'number {x} is not palindrome') 


# 2
# n = int(input("enter the number: "))
# rev = 0
# while n > 0:
#     ld = n%10
#     rev = rev*10+ld
#     n = n//10  
# print(rev)


# 3
# n = input("enter the string:")
# rev = n[::-1]
# if n ==rev:
#    print("string is palindrome")
# else:
#    print("string is not palindrome")



n = int(input("enter the number: "))
td,m,y = 0,n,n
sum = 0
while n> 0:
    td = td+1
    n=n//10
print(td)    
while  m>0:
   ld = m%10
   sum = sum+ld**td
   m = m//10
print(sum)
if y==sum:
  print(f'number {y} is armstrong') 
else:
   print(f'number {y} is not armstrong')  
