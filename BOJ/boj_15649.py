# N, M = map(int, input().split())

# num = [(i+1) for i in range(N)]
# check = [False] * N

# arr = []

# def dfs(cnt):
#     if(cnt == M):
#         print(*arr)
#         return
    
#     for i in range(N):
#         if(check[i]):
#             continue
        
#         check[i] = True
#         arr.append(num[i])
#         dfs(cnt + 1)
#         arr.pop()
#         print(arr)
#         print(check)
#         check[i] = False
        
# dfs(0)

import sys

input = sys.stdin.readline

def back():
    if len(answer) == m:
        print(*answer)
        return
    for i in range(1, n + 1):
        if not i in answer:
            answer.append(i)
            back()
            answer.pop()
n, m = map(int, input().split())

answer = []
back()

# 백트래킹 반드시해야해






















# 숫자 입력 → 문제의 요구사항 입력
# n, m 입력 / 정답 기록용의 s 리스트 생성
# 메서드 구현
# 주어진 n까지 중복 없이 m개를 골라 출력
# 리스트 s의 길이가 m과 동일해지면 해당 반복문을 멈추고 출력 후 종료
# 동일하지 않은 경우 for 반복문 실행( 1 ~ n + 1까지), i는 반복문에 할당된 변수
# 정답 기록용 배열의 리스트에 i를 추가
# 해당 dfs 메서드 실행
# 재귀호출된 메서드가 종료 후 s 리스트 안에 존재하는 원소를 pop

#백트래킹은 DFS(Depth-First Search, 깊이 우선 탐색)의 방식을 기반으로,
#불필요한 경우를 배제하며 원하는 해답에 도달할 때까지 탐색하는 전략
#백트래킹은 기본적으로는 모든 경우의 수를 탐색한다는 브루트 포스(Brute Force)
#전략을 취하지만, 처리 속도를 향상시키기 위한 가지치기(Pruning)가 중요한 역할을 한다.
#나무에서 불필요한 가지를 제거하듯이 백트래킹에서 가지치기를 잘 할수록
#불필요한 경우가 제거되어 처리 속도가 많이 향상된다.