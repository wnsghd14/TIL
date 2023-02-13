# import sys
# n = int(sys.stdin.readline())

# cnt = [0,0]

# for i in range(2,n+1): 
#     cnt.append(min(cnt[i//2]+i%2, cnt[i//3] + i%3) + 1)
# print(cnt)
# print(cnt[-1])
import sys
input = sys.stdin.readline
n = int(input())

dp = [0]*(n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[n])