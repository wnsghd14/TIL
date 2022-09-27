location = [list(map(int, input().split())) for _ in range(19)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if location[x-1][j] == 0: # 0일때 1 가로방향
            location[x-1][j] = 1
        else:                     # 1일때 0
            location[x-1][j] = 0

        if location[j][y-1] == 0: # 0일때 1 세로방향
            location[j][y-1] = 1  
        else:
            location[j][y-1] = 0  # 1일때 0

for i in range(19):
    for j in range(19):
        print(location[i][j], end=" ")
    print()
