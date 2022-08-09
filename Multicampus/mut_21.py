# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.
### Input

# ```
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# ```

### Output
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 1, 0],
#  [0, 1, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0, 0, 1],
#  [0, 1, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0]]
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
N,M = map(int,input().split())

matrix = [[0] * (N+ 1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

    graph[x].append(y)
    graph[y].append(x)

print(matrix)
print(graph)