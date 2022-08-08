a,b = map(int,input().split())
lit = list(map(int,input().split()))
result = []
for i in range(a):
    if lit[i] < b:
        result.append(lit[i])
print(*result)