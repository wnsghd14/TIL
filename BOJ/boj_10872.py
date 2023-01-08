T = int(input())
arr = []
for i in range(1,T+1):
    arr.append(i)

ans = 1
for n in arr:
    ans *= n
print(ans)
