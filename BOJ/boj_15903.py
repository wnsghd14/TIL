import sys
input = sys.stdin.readline

a,b = map(int, input().split())
arr  = list(map(int,input().split()))

for i in range(b):
    arr = sorted(arr)
    res = arr[0] + arr[1]
    arr[0] = res
    arr[1] = res

print(sum(arr))