month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

T = int(input())

for tc in range(1, T+1):
    ans = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        ans = d2 - d1
    else:
        for i in range(m1, m2+1):
            if i == m1:
                ans += (month[i] - d1)
            elif i == m2:
                ans += d2
            else:
                ans += month[i]
    print(f'#{tc} {ans+1}')
    # 메서드 datetime 을 사용해보고 싶은데 넘넘 어렵당..