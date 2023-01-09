
# 에라토스뭐시기
# 0,1 제외 2부터 +1씩 더해주며 그 배수에 해당하는 값들을 False로 바꿔준다.
# 구글링을 했다. 
import sys
input = sys.stdin.readline

T = int(input())

arr = []
m = 10 ** 6
# 소수 판별
for i in range(T):
    N = int(input())
    arr.append(N)
prime = [False,False] + [True] * (m-1)


# i*2로 시작하는 이유
# i = 5라고 가정해보면
# 그렇다면 i만 남겨두고 5의 배수를 모두 지우니까,  5*2, 5*3, ..., 5*n, ... 이 모두 지워짐.
# 하지만 5*2, 5*3,5*4 는 이미 2,3 배수를 지울 때 모두 지웠음을 알 수 있다 (같은 계산을 다시 해 줄 필요가 없음.)
# 고로 i*i부터 시작해도 무관하다.
# 2*i로 건너뛰는 이유도 마찬가지. 2의 배수를 모두 지웠기 때문에 2의 배수들은 계산할 필요가 없기 때문이다.

# 파티션
for i in range(2,int(m)+1):
    if prime[i]:
        for j in range(i*2,m**0.5+1,i): # 여기가 핵심이다 마지막 i 튜플은
                                        # 그 다음이 i만큼 증가해서 나타내는것이다.
            if prime[j] == True:
                prime[j] = False

for num in arr:
    cnt = 0
    for i in range((num//2)+1):
        if prime[i] and prime[num-i]: # 여러가지라면 b-a가 가장 큰 것을 출력을 해야하기 때문에
            cnt += 1
    print(cnt)