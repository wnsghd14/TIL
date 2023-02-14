import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
oil = list(map(int, input().split()))
mi = oil[0]
result = 0
for i in range(n-1):
    if mi > oil[i]:
        mi = oil[i]
    result += mi * arr[i]
print(result)