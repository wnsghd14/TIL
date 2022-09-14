import sys
sys.stdin = open("./swea/input.txt","r")

T=int(input())

def rotated(a, N):
  result = [[0]* N for _ in range(N)]

  for i in range(N):
    for j in range(N):
        result[i][j] = a[N-j-1][i]
    return result

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans90 = rotated(arr, N)
    ans180 = rotated(ans90, N)
    ans270 = rotated(ans180, N)

    print(f'#{tc}')
    for i in range(N):
        print("".join(map(str, ans90[i])),end=" ")
