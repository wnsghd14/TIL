# n = int(input())

# data = list(int(input()) for _ in range(n))

# cnt = 0
# stack = []

# for i in data:
#     while stack and stack[-1] <= i:
#         stack.pop()
#     cnt += len(stack)
#     stack.append(i)

# print(cnt)

import sys

input = sys.stdin.readline

N = int(input())
stack = []      # 옥상 스택
cnt = 0      # 결과값

h = int(input())
stack.append(h)
top = 0

for _ in range(N-1):
    h = int(input())

    while top > -1:
        if stack[top] > h:
            cnt += top + 1
            break

        stack.pop()
        top -= 1

    stack.append(h)
    top += 1

print(cnt)