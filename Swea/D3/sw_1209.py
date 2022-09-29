# 가로 세로 대각선으로 나눠서 해결해야한다.
# 대각선을 모르겠어서 구글링 함.
# 가로 세로 대각선의 값을 모두 result라는 리스트에 담아 최댓값을 구하는 식으로 생각해보았다.


import sys

sys.stdin = open('./Swea/D3/1209.txt','r')


for tc in range(1,11):
  T = int(input())
  arr = []
  result = []
  for i in range(100):
    arr.append(list(map(int,input().split())))
# print(arr)

  # 가로 구하기

  for i in range(100):
    sum1 = 0
    for j in range(100):
      sum1 += arr[i][j]
      result.append(sum1)
  # print(result)
  # 세로 구하기

  for i in range(100):
    sum2 = 0
    for j in range(100):
      sum2 += arr[j][i]
      result.append(sum2)
  # print(result)
  # 대각선 구하기

  for i in range(100):
    sum3,sum4 = 0,0
    sum3 += arr[i][i]   # 오른쪽 대각선
    sum4 += arr[i][99-i]  # 왼쪽 대각선
  result.append(sum3)
  result.append(sum4)
  # print(result)
  print(f'#{tc} {max(result)}')