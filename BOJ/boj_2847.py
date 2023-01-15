n = int(input())
arr = [int(input()) for _ in range(n)]
arr = arr[::-1]
t = arr[0]
ans = 0
for i in range(1, n):
    if t <= arr[i]:
        ans += arr[i] - t + 1
        arr[i] = t - 1
        
    t = arr[i]
    
print(ans)