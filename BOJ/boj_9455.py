# import sys
# input = sys.stdin.readline
# N = int(input())
# answer = []
# for _ in range(N):
#     ls = list(map(int, input().split()))
#     metrix = [list(map(int, input().split())) for _ in range(ls[0])]
#     array = [0] * ls[1]
#     cnt = 0 
#     for i in metrix:
#         temp = 0
#         for k in i:
#             if(k == 1):
#                 array[temp] += 1
#             else:
#                 cnt += array[temp]
#             temp += 1
#     answer.append(cnt)
# for i in answer:
#     print(i)

# 강사풀이
# 박스 = 1
# 빈공간 = 0
# 이동거리 = 1
# 열_개수 = 4
# 행_개수 = 5
# 박스_리스트 = [
#     [1,0,0,0],
#     [0,0,1,0],
#     [1,0,0,1],
#     [0,1,0,0],
#     [1,0,1,0]
# ]
# for x in range(열_개수):
#     for y in reversed(range(행_개수)):
#         # print(y,x)
#         # 만약 탐색하는 좌표에 박스가 있다면.
#         if 박스_리스트[y][x] == 박스:
#             # y + 1 -> 5 : 조건만족 X

#             # while y+1 != 행_개수 and 박스_리스트[y+1][x] == 박스:
#             #     박스_리스트[y][x] = 빈공간
#             #     박스_리스트[y+1][x] = 박스
#             #     y += 1
#             #     이동거리 += 1
#             while True:
#                 if y + 1 == 행_개수:
#                     break
#                 if 박스_리스트[y+1][x] == 박스:
#                     break

#                 박스_리스트[y][x] = 빈공간
#                 박스_리스트[y+1][x] =박스
#                 y += 1
#                 이동거리 += 1
# print(이동거리)