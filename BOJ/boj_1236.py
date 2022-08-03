# 문제
# 영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.

# 성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.

# 출력
# 첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.

# 예제 입력 1 
# 4 4
# ....
# ....
# ....
# ....
# 예제 출력 1 
# 4
# 예제 입력 2 
# 3 5
# XX...
# .XX..
# ...XX
# 예제 출력 2 
# 0
# 예제 입력 3 
# 5 8
# ....XXXX
# ........
# XX.X.XX.
# ........
# ........
# 예제 출력 3 
# 3



# import sys
# input = sys.stdin.readline
# 행렬로 값을 받아 열 먼저 검사하고 그다음 행을 일일히 검사하는 방식을 생각했습니다.

N, M = map(int,input().split())

matrix = [input() for _ in range(N)] # 행렬 만들어 입력 받고
print(matrix)
vert = 0 
hori = 0
for i in range(N):
    if 'X' not in matrix[i]: # 열 먼저 검사
        vert += 1 # 필요한 인원 1 보충
   # 행의 경우엔 값 하나씩 비교해야 함.
    if 'X' not in [matrix[i][j] for j in range(N)]: # 매트릭스 각행렬의 값은 str 이기때문에 한번더 list 를 씌워줬다.
        hori += 1 # 필요한 인원 1 보충
print(max(vert,hori)) # 각 행렬에 겹치지 않는 1명씩 있으면 된다. 

# 구분
# n, m = map(int,input().split())
# board = [] # list 

# for _ in range(n): # board 리스트에 값을 넣어줌.
#     board.append(input())

# a, b = 0, 0

# for i in range(n):
#     if "X" not in board[i]: # 열에서 X값을 먼저 찾아 줍니다.
#         a += 1

# for j in range(m): 
#     if "X" not in [board[i][j] for i in range(n)]: # 그 후 행렬의 값에서 X 가 없으면
#         b += 1

# print(max(a ,b))