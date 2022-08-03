import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)] # 행렬 1
memo = [[0]*(m+1) for _ in range(n+1)] # 행렬 2
T = int(input())
for i in range(1, n+1): # 누적합에서 중복되는 부분을 제거해 주어야 한다.
    for j in range(1, m+1): # 
        memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1]
for _ in range(T):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])
