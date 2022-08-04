
N = int(input())
lit = [list(input()) for _ in range(N)]
vert, hori  = 0, 0

for i in range(N):
    cnt = 0
    for j in range(N):
        if lit[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            hori += 1 
               
for i in range(N):
    cnt = 0
    for j in range(N):
        if lit[j][i] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            vert += 1
            
print(hori,vert)