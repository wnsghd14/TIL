# DFS, BFS 정리

```python
import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque
# 덱 호출은 bfs를 하기위해 필요하다. 
# 재귀 제한은 dfs를 하기위해 필요하다.

#인접 리스트가 주어질때 , 예를들어
n, m, v = map(int, input().split())  
# n개의 정점과 m개의 간선이 주어지고, 
# dfs와 bfs의 시작위치가 v인 상황이 입력으로 주어지는경우가 많다.
graph = [ [] * m for i in range(n + 1)] 
# [[]. [], [], .... []]  빈리스트 n+1개, 여기에 인접리스트 내용물을 넣는다.

for i in range(m): 
    u, v = map(int, input().split())  #보통 간선이 이렇게 주어진다.
    graph[u].append(v)
    graph[v].append(u) #양방향 간선일떄 이렇게한다.
#[ [], [1번정점과 연결된 정점들], [2번정점과 연결된 정점들] , ....., ]


for i in range(1, n + 1):
    graph[i].sort()

# 이렇게 정렬을 하지않으면, dfs, bfs가 정상적으로 작동하지않는다!!
# dfs,bfs를 구현하려고 사용하는 pop, popleft가 
# 이미 정렬을 필수로 요구하기떄문이다... 

--------------------------------------------------------------
visited = [False] * (n + 1) 

def dfs(start):
    visited[start] = True
    for adj in graph[start]:
        if not visited[adj]:
            dfs(adj)        

# graph[start] -> start번 정점과 연결된 정점들이 뭐가있는지 adj로 순회하는것. 
# 그러나, dfs는 첫번째것만 보고간다.
# dfs 자체가 제일깊은걸 보는거기때문에, 
# 들어간곳에서 첫번째(이걸 표현하기위해 위에서 그래프를 정렬한것이다!!)
# 들어간곳에서 첫번째 간선을 통해 더 깊은 정점으로 이동,
# 그 깊은정점에서 또 첫번쨰 간선을 통해 더 깊은정점으로 이동
# 이런 과정이 결국 재귀적이기때문에, dfs는 재귀로 표현이 가능한것이다 !!!
# 상술했듯, start번 정점과 연결된 정점중 "첫번째" 에서, 
# 두번째까지 탐색하지않고, 바로 dfs(adj)를 해버려서
# dfs(adj) -> visited[adj] = True가 되고 (자동으로 방문표시가됨)
# 다시 for adj2 in graph[adj] 가 되고.. 반복하는 것이다!!
dfs(v)                
-------------------------------------- 위까지가 dfs -----------
visited = [False] * (n + 1)
def bfs(start):                   

    visited[start] = True
    queue = deque([start])

    while queue:
        cur = queue.popleft()        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)
# bfs는 start로 부터 거리가 동일한 부분을 다 탐색하는식이다. 
# 역시 순서가 있다 (보통 오름차순같다)        
# 처음엔 입력된 start번 정점을 탐색한다. (cur = start)
# start번 정점을 하나하나 다 탐색한다. 
# 왜냐면 start번과 연결되어있는 각 정점 adj들은,
# 모두 start번 정점에서 거리가 1이기때문이다. 
# (거리가 1이라기보단 거리가 같다고 표현하는게맞겠다)                  
#그리고 방문정점을 표시하면서, 덱에 하나하나 방문정점을 넣어준다.                       
#그럼 다음번 반복되는 cur = queue.popleft()에서는, 
# queue 자체가 이미 start에서 거리가 1인 adj들로 구성이되어있고, 
# 2인걸 queue에 추가하더라도, 
# append의 특성상 큐의 가장 우측에 자리하게되고(추가되는것들이),
# 먼저 추가되었던 거리가 1인 adj들은 popleft()를 통해 '먼저!!' 빠져나오게된다.
bfs(v)
```
