N = int(input())
arr = []
arr1 = []

for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for j in range(N):
    arr1.append(arr[j]*(j+1))
print(max(arr1))