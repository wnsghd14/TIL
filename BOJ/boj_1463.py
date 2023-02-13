import sys
n = int(sys.stdin.readline())

cnt = [0,0]

for i in range(2,n+1): 
    cnt.append(min(cnt[i//2]+i%2, cnt[i//3] + i%3) + 1)
print(cnt)
print(cnt[-1])