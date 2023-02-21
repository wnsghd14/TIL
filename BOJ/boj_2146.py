from pprint import pprint
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k] 
            ny = y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                arr[nx][ny] = land
                
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
land = 1
for i in range(n):
    for j in range(n):
        
        if arr[i][j] == 1 and visited[i][j] == False:
            bfs(i, j)
            land += 1