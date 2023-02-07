# 1913 달팽이

n = 3
m = 6
dx = [1,0,-1,0]
dy = [0,1,0,-1]
x,y = -1 ,0
d = -1
arr = [[0]*n for _ in range(n)] + [[0,0]]
k = n*n
# print(arr)
for i in range(n*2 -1):
    d = (d+1) % 4
    for j in range(n):
        x += dx[d]
        y += dy[d]
        arr[x][y] = k
        
        if k == m:
            arr[-1][0] = x+1
            arr[-1][1] = y+1
        k-=1
    if not d or not d %2:
        n -=1
for i in range(len(arr)):
    print(*arr[i])