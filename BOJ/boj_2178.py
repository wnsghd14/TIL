from collections import deque
# import sys
# input = sys.stdin.readline
# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
queue = deque()
check = [[0]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
 
# 시작점
queue.append((0,0))
check[0][0] = 1
dist[0][0] = 1
 
while queue:
    x, y = queue.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] == 0 and a[nx][ny] == 1:
                queue.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1
                check[nx][ny] = True
 
print(dist[n-1][m-1])