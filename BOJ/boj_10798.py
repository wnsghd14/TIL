lit = [input() for _ in range(5)]
cnt = 0
if len(lit) > cnt:
    cnt = len(lit)
for i in range(15):
    for j in range(5):
        if i >= len(lit[j]):
            continue
        else:
            print(lit[j][i], end='')
