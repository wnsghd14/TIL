# from collections import deque

# N = int(input())
# M = int(input())

# matrix = [[0] * (N + 1) for _ in range(N + 1)]

# for _ in range(M):
#     u, v = map(int, input().split())
#     matrix[u][v] = 1
#     matrix[v][u] = 1

# i = 1
# cnt = 0
# virus = deque()
# virus.append(i)
# check = [1]

# while virus:
#     i = virus.popleft()

#     for j in range(N + 1):
#         if matrix[i][j] == 1:
#             if j not in check:
#                 virus.append(j)
#                 check.append(j)
#                 cnt += 1

# print(cnt)

from sys import stdin
read = stdin.readline
dic = {}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)