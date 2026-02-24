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
