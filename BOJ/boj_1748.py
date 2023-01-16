import sys
input = sys.stdin.readline
# n = int(input())

# arr = ''
# for i in range(1,n+1):
#     arr += str(i)
# # print(arr)
# print(len(arr))

# n = input()

# a = len(n)
# print(a)
# k = int(n) * a
# m = 9
# for i in range(1, a):
#     k -= m
#     m = m * 10+9
#     print(m)
# print(k)

N = int(input())
cnt = 0
step = 1

for i in range(N):
    if i + 1 == 10:
        step = 2
    elif i + 1 == 100:
        step = 3
    elif i + 1 == 1000:
        step = 4
    elif i + 1 == 10000:
        step = 5
    elif i + 1 == 100000:
        step = 6
    elif i + 1 == 1000000:
        step = 7
    elif i + 1 == 10000000:
        step = 8
    elif i + 1 == 100000000:
        step = 9
    cnt += step

print(cnt)