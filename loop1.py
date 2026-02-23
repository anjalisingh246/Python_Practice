#// <<- While - infinite Iteration
# syntax :-
# // while (condition):(infinite)
        # print( )
# increment / decerement

# // declare start point
# while (declare stop point):(finite)
        # print( )
# increment / decerement

# 1)  n = int(input("Enter the value: "))
# while n>2:
#     print("hello")

# 2)
# n = int(input("enter the value: "))
# x = 1
# while x<=10:
#     print(x*n, end = ' + ')
#     x= x+1
# output= 5 + 10 + 15 + 20 + 25 + 30 + 35 + 40 + 45 + 50 +


# 3) 
# n = int(input("enter the value: "))
# x = 1
# while x<=n:
#     if(x<n):
#      print(x, end = '+')
#     else:
#      print(x) 
#     x= x+1
# output  = 1+2+3+4+5


# 4)
# n = int(input("enter the value: "))
# sum=0
# x = 1
# while x<=n:
#     sum = sum+x
#     if(x<n):
#      print(x, end = '+')
#     else:
#      print(x, end = '=') 
#     x= x+1
# print(sum)    
# output  = 1+2+3+4+5=


# 5)
# n = int(input("enter the number: "))
# sum = 0
# x = 1
# while(x<=n):
#     sum = sum+x
#     if(x<n):
#        print(x, end = '+')
#     else:
#        print(x, end = '=')

n = int(input("enter the value: "))
multi = 1
x = 1
while x<=n:
    sum = multi*x
    if(x<n):
     print(x, end = '*')
    else:
     print(x, end = '=') 
    x= x*1
print(multi)  



#// <<- for - finite Iteration