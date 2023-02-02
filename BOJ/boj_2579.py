n = int(input())
s = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = int(input())

# 계단은 한 번에 한 개 or 두 개
# 세 개 연속 X
# 마지막 무조건 도착

if n == 1:
    print(s[n])

elif n == 2:
    print(s[1] + s[2])

else:
    d[1] = s[1]
    d[2] = s[1] + s[2]
    d[3] = max(s[2] + s[3], s[1] + s[3])


    for i in range(4, n+1):
        d[i] = max(d[i-3] + s[i] + s[i-1], d[i-2] + s[i])

    print(d)