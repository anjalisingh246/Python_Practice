
# n = int(input("enter the input: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
# output-
# 1
# 12
# 123
# 1234
# 12345

n = int(input("enter the input: "))
for i in range(1,n+1):
    x=1
    for j in range(1,i+1):
        print(x,end='')
        x=x+1
    print()
