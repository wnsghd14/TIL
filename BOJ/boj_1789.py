s = int(input())
n = 0
start = 0
while s >= n:
    start += 1
    n += start
    if s < n:
        break
print(start-1)