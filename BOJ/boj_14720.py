N= int(input())
cnt = 0
lit = list(map(int,input().split()))
for i in range(N):
    if lit[i] ==cnt % 3:
        cnt += 1
print(cnt)