# 11726 2xn타일링

n = int(input())

arr = [0]*(n+1)

if n == 1 or n == 2 or n == 3:
    print(n)
else:
    arr[1] = 1
    arr[2] = 2
    print(arr)
    for i in range(3,n+1):
        arr[i] = arr[i-1] + arr[i-2]
        print(arr)
    print(arr[i]%10007)
