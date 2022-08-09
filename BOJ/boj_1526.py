n = int(input())
while 1:
    cnt = 0
    for i in str(n):
        if i != "4" and i != "7":
            cnt = 1
            n -= 1
            continue
    if cnt == 0:
        print(n)
        break
