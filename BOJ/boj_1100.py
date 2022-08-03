#import sys
#input = sys.stdin.readline

# graph = [list(input().split()) for _ in range(8)] # 행~렬을 만들어 준다.
# cnt = 0
# for i in range(8): # 행렬값을 구하기 위해 이중for문 사용.
#     for j in range(8): 
#         if graph[i][j] == 'F' and (i+j) % 2 == 0: # 아까 알려주신대로 더한 값이 짝수일때
#             cnt += 1
# print(cnt)

# 런타임에러..

chess = [] # 체스판
horse = 0 # 말 올라가있는 갯수

for _ in range(8): # 8X8 
    chess.append(list(map(str,list(input())))) # 2중리스트 만들기.

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == 'F': #
            horse += 1
print(horse)