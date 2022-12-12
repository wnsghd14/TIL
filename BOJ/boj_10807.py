n = int(input())
lit = list(map(int,input().split()))
a = int(input())
ans = 0
for i in lit:
    if a == i:
        ans += 1
print(ans)