# # 문제
# 슈퍼 마리오 앞에 10개의 버섯이 일렬로 놓여져 있다. 
# 이 버섯을 먹으면 점수를 받는다.
# 슈퍼 마리오는 버섯을 처음부터 나온 순서대로 집으려고 한다.
# 하지만, 모든 버섯을 집을 필요는 없고 중간에 중단할 수 있다. 중간에 버섯을 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다. 따라서 첫 버섯을 먹지 않았다면, 그 이후 버섯도 모두 먹을 수 없다.
# 마리오는 받은 점수의 합을 최대한 100에 가깝게 만들려고 한다.
# 버섯의 점수가 주어졌을 때, 
# 마리오가 받는 점수를 출력하는 프로그램을 작성하시오.

# 입력
# 총 10개의 줄에 각각의 버섯의 점수가 주어진다. 
# 이 값은 100보다 작거나 같은 양의 정수이다. 
# 버섯이 나온 순서대로 점수가 주어진다.
# Ex:10,     1
#    20,     2
#    30,     3
#    40,     5
#    50,     8
#    60,     13
#    70,     21
#    80,     34
#    90,     55
#    100,    89

# 출력
# 첫째 줄에 마리오가 받는 점수를 출력한다. 
# 만약 100에 가까운 수가 2개라면 (예: 98, 102) 마리오는 큰 값을 선택한다.
# Ex: 100, 87

# 풀이

score = 0 # 점수 값 변수
mushrooms = [] # 점수를 넣을 리스트 
ex_score = 0 # 비교를 위한 변수
for j in range(10):
    mushrooms.append(int(input())) # 우선 다 넣는다.

for i in range(10):
    ex_score = score
    score += mushrooms[i]
    if score >= 100:
        u = 100 - ex_score #
        o = score - 100
        if o <= u:
            print(score)
            break
        else:
            print(ex_score)
            break
else:
    print(score)
# 준혁님 풀이
# m_list = [] # 점수를 담을 리스트
# m_big = 0

# for i in range(10):
#     m_list.append(int(input()))
# mush = sum(m_list)

# # 입력한 점수의 총합이 100과 같거나 넘지 않을경우 
# if mush <= 100:
#     print(mush)
# else: # 리스트의 역순으로 진행 
#     for j in range(9, -1, -1):
#         if mush > 100: # 점수가 100이 넘으면 
#             mush -= m_list[j] # 리스트 역순으로 sc에서 뺀다 
#         elif mush == 100: # 100일경우 종료 
#             break
#         else:
#             m_big = mush + m_list[j+1] # 아닐경우 sc에 직전의 값을 더한다. 
#             break

#     if mush == 100: # sc가 100이면 출력
#         print(mush)
#     else: # 아닐경우 (sc-100)의 절대값과 (sc_big-100) 
#         if abs(mush-100) >= abs(m_big-100):
#             print(m_big)
#         else:
#             print(mush)

