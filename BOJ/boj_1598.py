n, m = map(int,input().split())
if n % 4 == 0:
    a = 4 
    b = n // 4
else:
    a = n % 4
    b = n // 4 + 1
if m % 4 == 0:
    c = 4
    d = m // 4
else:
    c = m % 4
    d = m // 4 + 1
cnt = max(a,c) - min(a,c) + max(b,d) - min(b,d)
print(cnt)