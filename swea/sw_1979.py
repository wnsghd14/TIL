# N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

# [예제]

# N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때

# 길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.
# [제약 사항]

# 1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

# 2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


# [입력]

# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

# 다음 줄부터 각 테스트 케이스가 주어진다.

# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.

# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.

# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.

# 행렬을 받아 가로와 세로에서 k의 길이만큼만 나왔을때 result에 1을 더한다..
# 행과 열에서 비교하여 1인경우에 cnt 1을 더해주고 
# 만약 카운트값이 3에만 해당할 때 result 값에 1을 넣어준다.
import sys
sys.stdin = open('./Swea/input.txt','r')

T = int(input())

for test_case in range(1, T + 1):
  N, K = map( int, input().split())
  puzzle = [list(map(int, input().split())) for _ in range(N)] # 행렬 만들기
  result = 0
  # 행 기준
  for i in range(N):
    cnt = 0 # 값 초기화
    for j in range(N): 
      if puzzle[i][j] == 1: # 1일때
        cnt+=1 # 채울 수에 1을 추가
      else: # 1이 아닌 경우
        if cnt == K: # cnt 가 3일때 0을 만난다묜
          result += 1 # result를 바로 1 더해주고
        cnt = 0 # 값 초기화
    if cnt == K: # 고 전에 cnt 가 3이묜
      result +=1 # result 1 추가 따잇
  # print(result)
  # 열 기준
  for j in range(N):
    cnt = 0
    for i in range(N):
      if puzzle[i][j]==1:
        cnt += 1
      else:
        if cnt == K:
          result+= 1
        cnt = 0
    if cnt == K:
        result += 1
  # print(result)
  print(f"#{test_case} {result}")