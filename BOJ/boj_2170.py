import sys
input = sys.stdin.readline
li = []

ans = 0
n = int(input())

for i in range(n):
    a,b = map(int,input().split()) # 입력때문에 시간초과 났음
    li.append((a,b))
li.sort()
aa, bb = li[0][0], li[0][1]
for i in range(1, n):
    a,b = li[i][0], li[i][1]
    if a <= bb:
        bb = max(bb, b)
    else:
        ans += bb - aa
        aa, bb = a, b

ans += bb - aa

print(ans)