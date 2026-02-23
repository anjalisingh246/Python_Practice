n = int(input("enter the number: "))
a,b= 0,1
while n>0:
    print(a, end='  ')
    c = a+b
    a,b=b,c
    n=n-1

