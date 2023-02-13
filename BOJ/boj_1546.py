n = int(input())
arr = list(map(int,input().split()))

result = 0
for i in range(n):
    result += (arr[i]/max(arr))*100
print(result / n)