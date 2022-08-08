T = int(input())
for _ in range(T):
    n = int(input())
    N = int(input())
    for i in range(N):
        p,q = map(int,input().split())
        
        if p > 0:
            n += p*q
        elif p == 0:
            print(n)
    print(n)