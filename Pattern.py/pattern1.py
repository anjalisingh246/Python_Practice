# n = int(input("enter the number: "))
# i = 1
# while i<=n:
#     print("* "*n)
#     i = i+1

# Output-
# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for loop
n = int(input("enter the input: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('* ',end='')
    print()


