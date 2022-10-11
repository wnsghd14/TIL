import sys

sys.stdin = open("_퍼펙트셔플.txt")
# 홀수 짝수로 하여 나누면ㄴ 된다.
# 인덱스 값의 위치를 홀수 짝수의 값에서 변환 해주는 식인데, 막상해보면 조밥이다.
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(input().split())
    
    result = [0]*N # 카드길이만큼의 보드를 만든다.
    if N % 2 == 1: #홀수
        for i in range(N//2+1): # 우선 반으로 나눠주는데 1을 더해 빈공간을 만들어서 반으로 나눈후.5일경우 3:3 이여야함.
            result[2*i] = card[i] # card의 인덱스값을 result의 짝수 인덱스값으로 치환
            # print(i)
        for j in range(N//2): #나뉘어진 갯수길이에서 나머지 값 구하기.5일경우 2
            result[2*j+1] = card[j+N//2+1] # card 의 홀수 인덱스값을 result의 홀수 인덱스값으로 치환
            # print(j) 
    elif N % 2 == 0: # 짝수
        for k in range(N//2):
            result[2*k] = card[k] # card[2],reuslt[4] 의값을 치환.
            result[2*k+1] = card[k+N//2] # ex: card[1]의 값과 result[3]의 값을 치환. 
            # print(k)
    print(f'#{tc}',*result)