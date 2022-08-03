N = int(input())

for i in range(N):
    M = int(input())
    n = set(map(int,input().split()))
    m = int(input())
    t = list(map(int,input().split()))

    for j in t:
        if j in n:
            print(1)
        else:
            print(0)
