# arr == arr[::-1] 만 생각하면 되는데
# 싸늘하다.. 가슴에 인덱스 에러가 날아와 꽂힌.. 많이 뚜까맞고 찾은 사실
# list(zip( *arr ))
# 가로의 합은 평소대로 이중 for문 돌면서 구할 수 있지만, 세로의 합은 구하기가 좀 번거로웠다.
# 그럴 때 행과 열을 바꿔주면, 평소대로 이중 for문 돌면서 세로의 합도 구할 수 있다!
# 구씨.. 술만 퍼먹더니 멋쟁이었어.
import sys

sys.stdin = open('./Swea/D3/1215.txt','r')

for tc in range(1,11):
  T = int(input())
  arr = []
  result = 0
  for i in range(8):
    arr.append(list(input()))
    arr1 = list(map(list,zip(*arr)))
  # print(arr)
  # print(arr1)
  for i in range(8):
    for j in range(8 - T + 1):
      garo = arr[i][j:j + T]
      if garo == garo[::-1]:
        result += 1
      sero = arr1[i][j:j+T]
      if sero == sero[::-1]:
        result += 1
  print(f'#{tc} {result}')