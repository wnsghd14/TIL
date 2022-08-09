N,M = map(int,input().split())
matrix = [[0] * (N+1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int,input().split())
    matrix[x][y] = 1
    graph[x].append(y)

print(matrix)
print(graph)