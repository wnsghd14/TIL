import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    sen = list(input().split())
    ans = []
    for word in sen:
        ans.append(word[::-1])
    print(*ans, sep=' ')