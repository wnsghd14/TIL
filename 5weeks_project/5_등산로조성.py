import sys

sys.stdin = open("_등산로조성.txt")

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,1,-1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    lit = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0
    # def dfs(x):

    # for i in range(N):
    #     for j in range(N):
    #         if lit[i][j] > max_:
    #             max_ = lit[i][j]
    # dfs 너무어려웡 힝