arr = [list(map(int,input().split())) for _ in range(10)]


x, y = 1, 1

while True:
    if (arr[x][y] == 0):
        arr[x][y] = 9
    elif (arr[x][y] == 2):
        arr[x][y] = 9
        break

    if ((arr[x][y+1] == 1 and arr[x+1][y] == 1)):
        break

    if (arr[x][y+1] != 1):
        y = y + 1
    elif (arr[x+1][y] != 1):
        x = x + 1

for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()