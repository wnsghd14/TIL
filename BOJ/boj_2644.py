import sys
sys.setrecursionlimit(300000)

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)
            
n = int(input())
graph = [[] for _ in range(n+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
check = [0]*(n+1)
dfs(s)
print(check[e] if check[e] > 0 else -1)



n = int(input())

start,end = list(map(int,input().split()))

m = int(input())
# 빈 리스트를 n+1 개 가진 이차원 리스트
graph = [[] for _ in range(0,n+1)]
# _ 값을 사용하지않겠다는 의미
for _ in range(m):
    x, y = list(map(int,input().split()))
    # 공백을 기준으로 2개의 숫자가 입력되니
    graph[x].append(y)
    graph[y].append[x]
    # 무방향 인접그래프

# 방문표시 리스트
    visited = [False] *(n+1)

    # dfs 시작전 기본값
stack = []
stack.append(start)
visited[start] = True
# 스택이 비어있지않으면 반복
while len(stack) != 0:
    # LIFO , 스택의 가장 위에 있는 값을 저장
    number = stack.pop()
    if number == end:
        break
    # 해당하는 값의 인접 그래프를 저장
    adj_graph = graph[number]
    print(number,adj_graph)
    # 인접하는 값들을 탐색
    for adj_number in adj_graph:
        # 방문한적 없을때 스택에 값을 append
        if not visited[adj_number]:

            stack.append(adj_number)
            visited[adj_number] = True