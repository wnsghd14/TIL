T = int(input())
h = 0
m = 0
for tc in range(1, T + 1):
    num = list(map(int, input().split()))
    h = num[0] + num[2]
    m = num[1] + num[3]
    if m > 59:       # 리스트로 접근하는 방식.
        m -= 60
        h += 1
    if h > 12:
            h -= 12
    print('#{} {} {}'.format(tc, h, m))

# 각각을 int 로 하여 더해주기!
T = int(input())

for tc in range(1, T+1) :
    h1, m1, h2, m2 = map(int, input().split())

    m = m1 + m2
    h = h1 + h2 + m // 60
    m = m % 60
    if h > 12 :
        h = (h - 12)
    print("#{} {} {}".format(tc, h, m))