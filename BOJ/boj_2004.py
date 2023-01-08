# nCm = n! / (n-m)!m!
# 0이 생기는 경우는 10일때이다.
# 10은 2와 5의 곱이므로
# 2와 5가 몇번 나누어지는지를 구한 후 2와 5의 갯수중 더 작은 개수를 선택하면된다.

# 5가 몇번 나누어지는지
def Count1(n):
    answer = 0
    while n != 0:
        n = n // 5
        answer += n
    return answer

# 2가 몇번 나누어지는지
def Count2(n):
    answer = 0
    while n != 0:
        n = n // 2
        answer += n
    return answer


n, m = map(int, input().split())

if m == 0:
    print(0)

else:
    # 2와 5의 개수를 nCm을 구할 때처럼 구해서 더 작은 개수를 선택한다.
    result = min(Count2(n) - Count2(m) - Count2(n - m), Count1(n) - Count1(m) - Count1(n - m))
    print(result)
