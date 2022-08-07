import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
# 지금까지의 문제중 가장 손쉬운 문제.
# t = 그룹의 개수
# n = 행렬의 길이
# m = 1의 길이가 3일때 누워라
# 변수를 두개 잡아주고 행렬에서 답을 구한다.
# 단
t = int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    cnt = 0
    for i in range(n): # 행에서
        for j in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            if matrix[i][j] == 0 or j == n-1: # 0이거나 끝자리일때
                if cnt == m: # 계산한 카운트가 m이라면 3일때 3줄 말곤 안침.result에 1 넣어주기
                    result += 1
                cnt = 0 # 초기화를 해야함
    for j in range(n): # 열에서
        for i in range(n):       
            if matrix[i][j] == 1: # 똑같이 1이면 카운트
                cnt += 1
            if matrix[i][j] == 0 or i == n-1: # 여기선 i가 끝자리임
                if cnt == m: # 계산한 카운트가 m이라면 똑같이 result에 1을 넣어준다
                    result += 1
                cnt = 0 # 초기화 필수!
    print(f'#{tc} {result}')