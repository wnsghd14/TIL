import sys
input = sys.stdin.readline

n = int(input())

mines = [list(input().rstrip()) for _ in range(n)]
step = [list(input().rstrip()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
lose = False

for i in range(n):
    for j in range(n):
        cnt = 0
        if step[i][j] == 'x' and mines[i][j] == '.':
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or y < 0 or x >= n or y >= n:
                    continue
                
                if mines[x][y] == '*':
                    cnt += 1
            answer[i][j] = cnt
            
        if step[i][j] == 'x' and mines[i][j] == '*':
            lose = True

if lose:
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    print(*answer[i], sep='')