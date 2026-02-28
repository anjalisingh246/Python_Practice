def palindrome(x,rev):
   rev,a = 0,x
while x>0:
    n = x%10
    rev = rev*10 + n
    x = x//10
if rev==a:
    print("number is palindrome")
else:
    print("number is not palindrome")    
x = int(input("enter the nummber:"))
