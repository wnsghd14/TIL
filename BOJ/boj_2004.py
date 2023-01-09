# 처음에는 
# import sys, math


# N,M = map(int,input().split())
# arr = []
# arr1 = []
# for i in range(1,N+1):
#     arr.append(i)
# for i in range(1,M+1):
#     arr1.append(i)

# ans = 1
# arr2 = []
# for n in arr:
#     ans *= n
#     arr2.append(ans)
# arr3 = []
# for n in arr1:
#     ans *= n
#     arr3.append(ans)

# count = 0
# for i in range(len(arr2)):
#     if (arr2[i] == "0"):
#         count += 1
#     else:
#         break
# for i in range(len(arr3)):
#     if (arr3[i] == "0"):
#         count += 1
#     else:
#         break

# print(count)

# nCm = n! / (n-m)!m!
# 0이 생기는 경우는 10일때이다.
# 도무지 감이안잡혀서 구글링을 통해 알아봤다~
# 10은 2와 5의 곱이므로
# 2와 5가 몇번 나누어지는지를 구한 후 
# 2와 5의 갯수중 더 작은 개수를 선택하면된다.

# 5가 몇번 나누어지는지
# # 2가 몇번 나누어지는지
# 확인후 2와 5를 세서 더하고 빼고 한다
# 게중 가장 작은 수를 넣는다~
import sys
input = sys.stdin.readline

def count_cal(check, num):
    cnt = 0
    num1 = num
    while(check >= num1):
        cnt += check // num1
        num1 *= num
    return cnt

n, m = map(int, input().split())
# print(count_cal(n,2))
# print(count_cal(n-m, 2))
# print(count_cal(m, 2))
# print(count_cal(n, 5))
# print(count_cal(n-m, 5))
# print(count_cal(m, 5))
ans = min((count_cal(n, 2) - count_cal(n-m, 2) - count_cal(m, 2)), (count_cal(n, 5) - count_cal(n-m, 5) - count_cal(m, 5)))
print(ans)
# 지수로 구하는것이다
# 이항계수 (파스칼의삼각형)
# 이런문제를 내는 이유(추론을 해낼수 있는가)
# 5배수마다 1증가, 25배수마다 1증가, 125배수마다 1증가