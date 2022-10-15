import sys
sys.stdin = open('./Swea/D3/1220.txt', 'r')


for t in range(10):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for r in range(N):
        for c in range(N):

            if board[r][c] == 1:
                if r == (N - 1):
                    board[r][c] = 0
                else:
                    south = r
                    while south != (N - 1):
                        south += 1
                        if board[south][c] == 0:
                            if south == 6:
                                board[r][c] = 0
                        elif board[south][c] == 1:
                            break
                        elif board[south][c] == 2:
                            cnt += 1
                            break

    print(f'#{t + 1} {cnt}')