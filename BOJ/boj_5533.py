# import sys
# input = sys.stdin.readline()


N = int(input())
# 처음엔 한꺼번에 리스트로 넣어서 했는데 접근이 너무 어려웠음. 그래서 셋으로 나눔
firstgame = []
secondgame = []
thirdgame = []

answer = [0] * N

for i in range(N):
# 처음엔 한꺼번에 리스트로 넣어서 했는데 접근이 너무 어려웠음. 그래서 셋으로 나눔
    first, second, third = map(int, input().split()) 
    firstgame.append(first)
    secondgame.append(second) # 각각의 리스트값을 리스트에 넣으며 나눠 주기(행렬?)
    thirdgame.append(third)

for j in range(N):
    score = 0
    if firstgame.count(firstgame[j]) == 1: # 열에서 유일하게 다른값이 있으면 더해주기
        score += firstgame[j]
    if secondgame.count(secondgame[j]) == 1:# 똑
        score += secondgame[j]
    if thirdgame.count(thirdgame[j]) == 1: # 같다
        score += thirdgame[j]
    
    print(score) # 구한 값을 for문 내에서 출력

