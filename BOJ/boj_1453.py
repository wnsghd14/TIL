T = int(input())
cnt = 0
ls = list(map(int,input().split()))
lit = [0]*101
    # print(lit)
for i in ls:
    if lit[i] == 0:
        lit[i] += 1
    else:
        cnt += 1
print(cnt)
