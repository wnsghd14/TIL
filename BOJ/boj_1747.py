n = int(input())
m = 1000000

prime = [False,False] + [True] * (m-1)
for i in range(2, int(m **0.5)+1):
    if prime[i]:
        for j in range(i+i,m+1,i):
            if prime[j]:
                prime[j] = False

res = 0
for i in range(n, m+1):
    if i == 1:
        continue
    if str(i) == str(i)[::-1]:
        if prime[i]:
            res = i
            break
if res == 0:
    res = 1003001
print(res)