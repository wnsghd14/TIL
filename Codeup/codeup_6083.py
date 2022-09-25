r,g,b = map(int,input().split())
0 <= r,g,b <= 127
cnt = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(f'{i} {j} {k}')

            cnt += 1
print(cnt)