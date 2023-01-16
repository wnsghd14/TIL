
N = int(input())
num = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

value = 1
a = int(N / 2)
b = int(N / 2)
arr[a][b] = value

tmp = int(N / 2)
for i in range(tmp):
    # 위로 이동
    for _ in range(2 * i + 1):
        value += 1
        a -= 1
        arr[a][b] = value
    # 오른쪽으로 이동
    for _ in range(2 * i + 1):
        value += 1
        b += 1
        arr[a][b] = value
    # 아래로 이동
    for _ in range(2 * i + 2):
        value += 1
        a += 1
        arr[a][b] = value
    # 왼쪽으로 이동
    for _ in range(2 * i + 2):
        value += 1
        b -= 1
        arr[a][b] = value

for _ in range(2 * (tmp - 1) + 2):
    value += 1
    a -= 1
    arr[a][b] = value

x = 0
y = 0
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
        if arr[i][j] == num:
            x = i + 1
            y = j + 1
    print()

print(x, y)