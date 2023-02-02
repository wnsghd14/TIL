import sys

n = int(sys.stdin.readline())
m = [0] * 301

for k in range(n):
    m[k] = int(sys.stdin.readline())

dp = [0] * 301 # 계단
dp[0] = m[0] # 첫 번째 계단
dp[1] = m[0] + m[1] # 두 번째 계단
dp[2] = max(m[1] + m[2], m[0] + m[2]) # 연속으로 세 개의 계단을 밟는 경우와 두 계단을 한번에 오르는 경우를 비교

# 반복문을 통해 계단을 오른다.
for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + m[i - 1] + m[i], dp[i - 2] + m[i]) # 연속으로 세 개의 계단을 밟는 경우와 두 계단을 한번에 오르는 경우를 비교

print(dp[n - 1])