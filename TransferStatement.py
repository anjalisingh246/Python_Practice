# x ='A'
# y = chr(ord(x)+1)
# print(y)

# n = int(input("enter the number: "))
# for i  in range(1,n+1):
#     ch='A'
#     for j in range(1,i+1):
#         print(ch,end='')
#         ch =chr(ord(ch)+1)
#     print()    
# output-
# A
# AB
# ABC
# ABCD
# ABCDE


# n = int(input("enter the number: "))
# ch='A'
# for i  in range(1,n+1): 
#     for j in range(1,i+1):
#         print(ch ,end=' ')
#         ch =chr(ord(ch) +1)
#     print()    

# output-
# A
# BC
# DEF
# GHIJ
# KLMNO    

# n = int(input("enter the value:"))
# i =1
# while i<=n:
#     if i==3:
#       i=i+1
#       continue
#     print(i)
#     i = i+1

# n = int(input("enter the value:"))
# i =1
# while i<=n:
#     if i==3 or i==5:
#       i=i+1
#       continue
#     print(i)
#     i = i+1

n = int(input("enter the value:"))
i =1
while i<=n:
    if i==3:
      pass
    print(i)
    i = i+1

# n = int(input("enter the value:"))
# i =1
# while i<=n:
#     if i==3:
#       i=i+1
#       break
#     print(i)
#     i = i+1