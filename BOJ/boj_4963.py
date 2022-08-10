from collections import deque

dx = [1,-1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1,1,-1,1]
queue = deque()

def bfs(x,y):
    queue.append((x, y))




while True:
    n, m = map(int,input().split())
    if (n,m) == (0,0):
        break
    lit = [list(map(int,input().split())) for _ in range(m)]
    visit = [[False]*n for _ in range(m)]
    