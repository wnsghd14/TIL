# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

# 아래는 N=5 의 예이다.
 



# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.

# 죽은 파리의 개수를 구하라!

# 예를 들어 M=2 일 경우 위 예제의 정답은 49마리가 된다.
 



# [제약 사항]

# 1. N 은 5 이상 15 이하이다.

# 2. M은 2 이상 N 이하이다.

# 3. 각 영역의 파리 갯수는 30 이하 이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.


# [출력]

# 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# for 문에서 arr(M,M)부터 arr(2M,2M) 까지 합만을 더해주면 된다고 생각해서
# 간단하게 풀어보려다가 완전히 낭패를 .. 
# 하다보니 4중 포문 까지 가서야 해결완료!

import sys
sys.stdin = open('./Swea/input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N-M+1): # 시작 좌표
        for j in range(N-M+1):
            chae = 0
            for t in range(i,i+M):# 끝 좌표
                for k in range(j,j+M):
                    chae += arr[t][k]
            if chae > result:
                result = chae
    print(f'#{tc} {result}')