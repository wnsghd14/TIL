arr = []
for i in range(1,10):
    n = int(input())
    arr.append(n)
ans = max(arr)
ans2 = arr.index(ans)+1
print(ans)
print(ans2)