from collections import deque

N = int(input())
M = int(input())

matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1

i = 1
cnt = 0
virus = deque()
virus.append(i)
check = [1]

while virus:
    i = virus.popleft()

    for j in range(N + 1):
        if matrix[i][j] == 1:
            if j not in check:
                virus.append(j)
                check.append(j)
                cnt += 1

print(cnt)