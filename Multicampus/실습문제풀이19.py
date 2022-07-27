number = map(int,(input()))

cnt = 0

for i in number:
    if i > 0:
        cnt += 1

print(cnt)