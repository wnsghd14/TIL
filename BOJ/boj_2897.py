N, M = map(int, input().split())

parking = [list(input()) for _ in range(N)]

dx = [0, 0, 1, 1] #제자리, 오른쪽, 아래, 오른쪽아래
dy = [0, 1, 0, 1]

answer = {  
    0:0,   # 차를 안부수고 주차 
    1:0,   # 1대 부수고 주차
    2:0,   # 2대 부수고 주차
    3:0,   # 3대 부수고 주차
    4:0    # 4대 부수고 주차
}


valid = True # 건물을 발견했을 때 체크할 목적으로 boolean 사용
for i in range(N-2+1): 
    for j in range(M-2+1):
        cnt = 0 # 차 대수
        for d in range(4):
            r = i + dx[d]
            c = j + dy[d]
            if parking[r][c] == '#':
                valid = False  # 건물을 발견하면 False로 변경 
                break
            elif parking[r][c] == 'X':
                cnt += 1
                valid = True # 차를 발견하면 
            valid = True # '.' 일때도 True
        if valid :  # True 일때 cnt를 answer에 저장 (각 지점마다 dx,dy를 다 순회후 False이면(건물발견했으면) 저장하지않아도된다)
            answer[cnt] += 1

print(*answer.values(), sep='\n')