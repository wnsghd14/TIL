T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = [[0]*N for _ in range(N)]

    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]
    x,y = 0,0
    way = 0
    for n in range(1, N**2+1): # 3 일때 3칸씩 총 9개니까.
        result[x][y] = n
        fx = x + dx[way]
        fy = y + dy[way]

        if fx not in range(N) or fy not in range(N) or result[fx][fy] != 0:
            way = (way + 1) % 4
        x += dx[way]
        y += dy[way]

    print(f'#{tc}')
    for row in result:
        print(*row)