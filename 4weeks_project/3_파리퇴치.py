import sys

sys.stdin = open("_파리퇴치.txt")
# T = 10개의 테스트 케이스
# n = 행렬의 길이(?)
# m = 파리를 잡는 작은 행렬의 길이(?)
# 어쨋든 N에서 M크기의 행렬이 돌다가 가장 큰 값의 행렬이 만들어 졌을때
# 미리 지정해둔 리스트에 append 후 그 리스트의 합의 값을 출력하면 된다고 생각함.
# 반복문을 돌때 그 인덱스 값과 m의 합이 n 을 넘어서면 안되기 때문에 break를 걸기.
# 또한 sum(list)로 각 자리에서 파리채 크기로 죽인마리수를 구하여 그중 제일 큰 수를
# 뽑아내어 출력
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 
    for i in range(N):
        if i + M > N:
            break
        for j in range(N):
            # print(sum_list)
            sum_list = [] # 항상 초기화를 하여야 해서 리스트를 여기다가 생성.
            if j + M > N:
                break
            for k in range(i, i + M): # i와
                for h in range(j, j + M): # j 에서 
                    sum_list.append(fly[k][h])
                    # print(sum_list) # 모든 list에 각 인덱스에서의 값을 더해주는데
            if max_sum < sum(sum_list): # 모든 인덱스에서 max_sum 이 더 크면 그게 가장 큰수이겠지 ?
                max_sum = sum(sum_list)
    # print(max_sum)
    print(f'#{tc} {max_sum}')