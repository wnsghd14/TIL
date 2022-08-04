m = int(input())
ls = [0,1,2,3]

for _ in range(m):
    x, y = map(int, input().split())
    ls[x], ls[y] = ls[y], ls[x]

print(ls.index(1))