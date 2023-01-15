import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    max = 0
    for num in nums[::-1]:
        if max < num:
            max = num
        elif max > num:
            ans += max-num
    print(ans)