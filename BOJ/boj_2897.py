r, c = map(int, input().split())

park = []
for _ in range(r):
    park.append(list(input()))

dy = [1, 0, 1]
dx = [0, 1, 1]

result = [0] * 5

for y in range(r):
    for x in range(c):
        if park[y][x] != '#':
            s = ""
            s += park[y][x]

            for i in range(3):
                ny = y + dy[i]
                nx = x + dx[i]

                if not (-1 < ny < r and -1 < nx < c):
                    break

                if -1 < ny < r and -1 < nx < c:
                    if park[ny][nx] == '#':
                        break

                    s += park[ny][nx]

            if len(s) == 4:
                result[s.count('X')] += 1

print(*result, sep='\n')