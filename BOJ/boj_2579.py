import sys

n = int(sys.stdin.readline())
m = [0] * 301

for k in range(n):
    m[k] = int(sys.stdin.readline())

dp = [0] * 301

dp[0] = m[0] 
dp[1] = m[0] + m[1] 

dp[2] = max(m[1] + m[2], m[0] + m[2]) 

for i in range(3, n + 1):
    
    dp[i] = max(dp[i - 3] + m[i - 1] + m[i], dp[i - 2] + m[i])

print(dp[n - 1])