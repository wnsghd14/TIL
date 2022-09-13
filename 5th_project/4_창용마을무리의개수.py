import sys

sys.stdin = open("_창용마을무리의개수.txt")


T = int(input())
for tc in range(1,T+1): # input 을 그냥 다받아 보았다.
    n, m = map(int, input().split())
    graph = [[0] for _ in range(n+1)] # [0] 보드를 만들고 1부터 N까지이니.
    visit = [False for _ in range(n+1)] # False 보드를 만들어서 dfs 방문판별
    cnt = 0 #무리의 수 카운트
    
    def dfs(x): # dfs 정의하기.
        visit[x] = True 
        for i in graph[x]: 
            if visit[i] == False: 
                dfs(i) # difs 재귀
# 인접리스트로 접근
    for _ in range(m): # 
        x, y = map(int, input().split()) 
        graph[x].append(y)
        graph[y].append(x)
    
    for j in range(1,n+1):
        if visit[j] == False: # 방문하지 않은곳이 있으면.
            cnt += 1 # cnt += 1
            dfs(j)

    print(f'#{tc} {cnt}')