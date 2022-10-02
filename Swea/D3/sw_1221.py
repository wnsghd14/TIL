import sys

sys.stdin = open('./Swea/D3/1221.txt','r')
t = int(input())

info = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for tc in range(1, t + 1) :
    num, n = input().split()
    arr = list(input().split())

    for i in range(int(n)) :
        arr[i] = info.index(arr[i])

    arr.sort()
    for i in range(int(n)) :
        arr[i] = info[arr[i]]

    print(f'#{tc}')
    print(*arr)