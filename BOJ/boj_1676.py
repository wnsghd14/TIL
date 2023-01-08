T = int(input())
arr = []
for i in range(1,T+1):
    arr.append(i)

ans = 1
for n in arr:
    ans *= n
cnt = 0
for i in str(ans)[::-1]:
    if i != '0':
       break
    cnt += 1
print(cnt)
