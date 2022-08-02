import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for tc in range(1,T+1):
    a,b,c = map(int,input().split())
    # print(a,b,c)
    d = 0
    if a == c:
        d += b
    elif a == b:
        d += c
    elif b == c:
        d += a
    print(f'#{tc} {d}')