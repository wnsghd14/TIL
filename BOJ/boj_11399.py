n = int(input())
t = list(map(int, input().split()))
num = 0
t.sort()
for i in range(n):
    for j in range(i + 1):
        num += t[j]
print(num)