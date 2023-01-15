n = int(input())

arr = list(map(int, input().split()))
arr1 = list(map(int, input().split()))

a = sorted(arr, reverse=True)
b = sorted(arr1)

s = 0
for i in range(n):
    s += a[i] * b[i]

print(s)