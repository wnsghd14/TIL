T = int(input())
for t in range(1,T+1):
    n = int(input())
    speed = 0
    move = 0
    for _ in range(n):
        arr = list(map(int,input().split()))
        if arr[0] == 1:
            speed += arr[1]

        elif arr[0] == 2:
            if speed > arr[1]: 
                speed -= arr[1]
            else:
                speed = 0
        move += speed

    print('#{} {}'.format(t, move))