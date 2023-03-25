n, m = map(int, input().split())
box = [0]*n

for _ in range(m) :
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        box[i-1] = c
for i in range(n):
    print(box[i], end=' ')