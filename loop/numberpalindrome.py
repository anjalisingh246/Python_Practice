n = int(input("enter the number: "))
rev,x = 0,n

while n > 0:
    ld = n%10
    rev = rev*10+ld
    n = n//10  
if rev==x:
      print(f'number {x} is palindrome') 
else:
     print(f'number {x} is not palindrome') 