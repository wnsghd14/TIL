# import sys
# input = sys.stdin.readline

# m = int(input())

# for x in range(m):
#     n = int(input())
#     ans = 0

#     for i in range(1,n+1):
#         ans += (n//i)*i  # 17427 번을 똑같이 가져왔다~

#     print(ans)
# 1억번 안에 해내는거면 시간초과가 안남 왜나냐 근데

# 현식님 답안
# import sys

# input = sys.stdin.readline

# # 자연수의 범위
# p = 10 ** 6

# # 약수들의 합을 위한 리스트
# measure = [1] * (p + 1)

# # 문제에서 요구하는 g(x)를 위한 리스트
# hap = [0] * (p + 1)

# # 모든 약수들의 합을 메모제이션 즉, 리스트 값을 미리 계산해서 저장해두기 위함이다.
# # 매번 값을 구하기 위해 반복문을 돌리는 것보다 미리 돌려놓고 그 값을 갖고 오는게 시간효율상 빠르기 때문이다.
# for i in range(2, p + 1):
#     for j in range(i, p + 1, i):
#         # j값은 i로 나누어 지는 값이기 때문에 measure[j]에 i값을 더해준다.
#         measure[j] += i
# # 정답을 위한 리스트
# answer = []

# # g(x)를 구하는 과정
# for i in range(1, p + 1):
#     # hap[i]는 i - 1 있던 값과 f(i) 값을 지속적으로 더 한 값이다.
#     hap[i] = hap[i - 1] + measure[i]

# # 반복문 안에 int(input())을 받아서 반복문 진행
# for _ in range(int(input())):
#     # n값 입력
#     n = int(input())
#     # 해당 되는 g(n) 값을 answer에 넣어준다 (넣어주고 보여주는게 더 빠를 거라고 생각이 들었다.)
#     answer.append(hap[n])
# # 정답출력
# for i in answer:
#     print(i)


import sys
input = sys.stdin.readline

ans=[0 for _ in range(1000001)] # 백만개의 리스트를 만든다~

for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        ans[j] += i
    ans[i] += ans[i-1]

T=int(input())

for _ in range(T):
    N=int(input())
    print(ans[N])