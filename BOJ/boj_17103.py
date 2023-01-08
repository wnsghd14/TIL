
# 6 = 1
# 8 = 1
# 10 = 3+7, 2 
# 12 = 5+7 , 2 
# 100 = 2+98
import sys
input = sys.stdin.readline

T = int(input())
arr = []
for i in range(T):
    N = int(input())
    arr.append(N)
    m = max(arr)
prime = [False,False] + [True] * (m-1)
print(m)
for i in range(2,int(m**0.5)+1):
    if prime[i]:
        for j in range(i+i,m+1,i):
            if prime[j]:
                prime[j] = False
for num in arr:
    cnt = 0
    for i in range((num//2)+1):
        if prime[i] and prime[num-i]:
            cnt += 1
    print(cnt)