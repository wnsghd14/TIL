# 1990 소수인팰린드롬
n,m = map(int,input().split())
m = min(10000000,m)
prime = [False,False] + [True]*(m-1)

for i in range(2,m+1):
    if prime[i]:
        k = str(i)
        for j in range(2*i,m+1,i):
            prime[j] = False
        if k == k[::-1] and i >= n:
            print(k)
print(-1)
