import sys

sys.stdin = open("_민석이의과제체크하기.txt")
# T = 두가지 조
# n = 조의 총 구성원
# m = 과제를 낸 사람.
# ls = 과제를 제출한 사람.
# 그래서 n의 범위에서 ls 에 해당하지 않는 학생을 result 변수에 넣어주어 출력하는 식으로 생각해봄. 
T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    ls = list(map(int,input().split())) # 같은 map(int) 로 받으니 오류가 떠서 리스트로 받음
    result = []
    for i in range(1,n+1): # 0말고 1부터 시작하기 때문에! 
        if i not in ls: # 이러면 시간 오래걸린다던데 다른방식으론어떤게있을까 생각합니다.
            result.append(i)
    # print(result)
    print(f'#{tc}',end=' ')
    print(*result) # 시퀀스 언패킹 연산자 사용