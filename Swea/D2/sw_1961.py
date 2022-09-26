import sys
sys.stdin = open("./Swea/input.txt","r")


def rotated(arr): # 90도로 돌아가는 것을 함수화
  result = [[0]*N for _ in range(N)] # 빈 행렬을 만들고

  for i in range(N):
    for j in range(N):
      result[i][j] = arr[N-1-j][i] # 빈행렬에 부모 행렬의 90도 꺾은 값을 넣어준다.ex)N=3 result[0][0] = arr[2][0] 요런식.
  return result

T = int(input()) # 몇개의 케이스를 볼것인가.

for tc in range(1,T+1): # tc 개의 케이스
  N = int(input()) # 행렬을 만들 숫자

  arr = [list(map(int,input().split())) for _ in range(N)] # 
  # N 숫자 크기의 행렬
  ans90 = rotated(arr) # 90도
  ans180 = rotated(ans90) # 90+90 이니 180
  ans270 = rotated(ans180) # 180 + 90 270도

  print(f'#{tc}')
  for a,b,c in zip(ans90,ans180,ans270): # zip으로 각 값을 묶어 a,b,c  를 출력인디.. 잘 몰르겠다.
    print(f'{"".join(map(str, a))} {"".join(map(str, b))} {"".join(map(str, c))}')
