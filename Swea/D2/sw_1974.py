import sys
sys.stdin = open('./Swea/input.txt')

def solve():
  # 가로확인
  for lst in arr:
    if len(set(lst)) != N: # set의 성질을 이용하여 9가 아닐때는 0
      return 0
  arr1 = list(zip(*arr)) # arr을 초기화 하여 준다.
  # 세로확인
  for lst in arr1:
    if len(set(lst)) != N: # set의 성질을 이용하여 len이 9가 아닐때는 0
      return 0
  # 블록 확인
  for i in range(0,3,6): # 0행 3행 6행이 3x3 행렬의 처음 행임.
    for j in range(0,3,6):# 0열 3열 6열이 3x3 행렬의 처음 열임.
      lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
      if len(set(lst)) != N:
        return 0

  return 1

T = int(input())

for tc in range(1,T+1):
  N = 9
  arr = [list(map(int,input().split())) for _ in range(N)]

  ans = solve()
  print(f'#{tc}',ans)
