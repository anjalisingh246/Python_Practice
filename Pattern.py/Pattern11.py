# n = int(input("enter the input: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()

# output-
# 1
# 22
# 333
# 4444
# 55555    


# n = int(input("enter the input: "))
# for i in range(1,n+1):
#     x=2
#     for j in range(1,i+1):
#         print(x ,end=' ')
#         x=x+2
#     print()

# Output-
# 2 
# 2 4
# 2 4 6
# 2 4 6 8
# 2 4 6 8 10    


n = int(input("enter the input: "))
for i in range(1,n+1):
    x=1
    for j in range(1,i+1):
        print(x ,end=' ')
        x=x+2
    print()

# output-
# 1 
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9    