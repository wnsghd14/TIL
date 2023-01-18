# N = int(input())
# num = int(input())
# arr = [[0] * N for _ in range(N)]

# value = 1
# a = int(N / 2)
# b = int(N / 2)
# arr[a][b] = value

# tmp = int(N / 2)
# for i in range(tmp):
#     # 위
#     for _ in range(2 * i + 1):
#         value += 1
#         a -= 1
#         arr[a][b] = value
#     # 오
#     for _ in range(2 * i + 1):
#         value += 1
#         b += 1
#         arr[a][b] = value
#     # 아
#     for _ in range(2 * i + 2):
#         value += 1
#         a += 1
#         arr[a][b] = value
#     # 왼
#     for _ in range(2 * i + 2):
#         value += 1
#         b -= 1
#         arr[a][b] = value
# x = 0
# y = 0
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=" ")
#         if arr[i][j] == num:
#             x = i + 1
#             y = j + 1
#     print()

# print(x, y)

n = int(input())
f = int(input())

# 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = -1, 0
d = -1
k = n ** 2

arr = [[0]*n for _ in range(n)] + [[0,0]]
for _ in range(2*n-1):
    d = (d + 1) % 4 # 0, 1, 2, 3
    for _ in range(n):
        x += dx[d]
        y += dy[d]
        print(x,y)
        arr[x][y] = k
        print(arr)
        if k == f:
            arr[-1][0] = x + 1
            arr[-1][1] = y + 1
        k -= 1
    if not d or not d % 2:
        n -= 1
print(*arr, sep='\n')