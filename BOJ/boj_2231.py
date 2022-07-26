T = int(input())
result = 0 # T 와 비교할 변수
for i in range(1, T + 1): # 모든 경우의 수 확인하기.
    N = list(map(int, str(i))) # str함수로 각 자리수를 N에 넣기
    result = i + sum(N) # i + 각자리의 합.
    if result == T: # i + 각자리의 합이 입력값이라면 프린트
        print(i)
        break
    if i == T: # 도달시 0출력
        print(0)