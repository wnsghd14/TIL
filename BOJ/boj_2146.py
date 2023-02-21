import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    global land
    maps[a][b] = land
    visit[a][b] = 1

    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and maps[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                maps[nx][ny] = land

def check(k):
    global ans
    dis = [[-1] * n for _ in range(n)]
    queue = deque()


    for i in range(n):
        for j in range(n):
            if maps[i][j] == k:
                queue.append((i, j))
                dis[i][j] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] > 0 and maps[nx][ny] != k:

                    ans = min(ans, dis[x][y])
                elif not maps[nx][ny] and dis[nx][ny] == -1:
                    dis[nx][ny] = dis[x][y] + 1
                    queue.append((nx, ny))
    
n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]

land = 1

for i in range(n):
    for j in range(n):
        if not visit[i][j] and maps[i][j]:
            bfs(i, j)
            land += 1

ans = sys.maxsize

for i in range(1, land):
    check(i)
print(ans)