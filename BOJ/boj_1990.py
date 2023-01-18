n, m = map(int, input().split())
# 1억안에 되는지 안되는지 의심을 먼저 해봐야한다.
# 허용범위내에서 가장 큰수덩이 부터 천천히 내려간다. (1억이면 천만)
m = min(10000000, m)

prime = [False,False] + [True] * (m-1)


for i in range(2, m+1):
    if prime[i]:
        k = str(i)
        if k == k[::-1] and i >= n:
            print(i)
        for j in range(2 * i, m + 1, i):
            prime[j] = False
print(-1)
# for i in range(2, int(m **0.5)+1):
#     if prime[i]:
#         for j in range(i+i,m+1,i):
#             if prime[j]:
#                 prime[j] = False
# if n % 2 == 0:
#     n += 1

# res = 0

# for i in range(n, m+1):
#     if i == 1:
#         continue
#     if str(i) == str(i)[::-1]:
#         if prime[i]:
#             res = i
#             print(res)

# print(-1)

a ,b = map(int,input().split())
m = 10 ** 7
p = [0,0] + [1] * (m-1)
for i in range(int(b**.5) + 1):
 if p[i]:p[i*i::i] = [0] * (m // i-i+1)
def f(n,r=0):
    while n:r *= 10; r+=n%10; n//=10
    return r
for i in range(a,min(b+1,m)):
    if p[i]and i==f(i):print(i)
print(-1)