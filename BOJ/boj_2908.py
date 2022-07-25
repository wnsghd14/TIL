# https://www.acmicpc.net/problem/2908
# import sys

# sys.stdin = open("1_상수.txt")
a, b = input().split() 
A = int(a[::-1])
B = int(b[::-1])
# 받은 두수를 거꾸로!
if A > B:
    print(A)
else:
    print(B)