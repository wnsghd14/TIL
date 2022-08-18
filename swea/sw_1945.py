T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a,b,c,d,e = 0,0,0,0,0
    while (N != 1):
        if N % 2 == 0:
            a += 1
            N = N / 2
        elif N % 3 == 0 :
            b += 1
            N = N/3
        elif N % 5 == 0 :
            c += 1
            N = N/5
        elif N % 7 == 0 :
            d += 1
            N = N/7
        elif N % 11 == 0 :
            e += 1
            N = N/11
    print(f'#{tc} {a} {b} {c} {d} {e}')