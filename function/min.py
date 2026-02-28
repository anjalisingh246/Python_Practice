# S = 'abcde'
# min_ascii_v = 255
# for ch in S:
#     x = ord(ch)
#     if min_ascii_v > x:
#         min_ascii_v = x
# print(chr(min_ascii_v))      


def a_min(S):
    min_ascii_v = 255
    for ch in S:
        x = ord(ch)
        if min_ascii_v > x:
            min_ascii_v = x
    print(chr(min_ascii_v))  
S = input("enter the value:")  
a_min(S)      