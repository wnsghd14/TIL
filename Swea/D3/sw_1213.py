# 보자마자 인풋받고 카운트 함수 쓰면 되겠다 ! 생각했음.
# 근데 인풋이 받아지질 않아서 vs코드가 알려주는대로 했더니 encoding이 필요하다고 했다.
# 이런것도 있구낭.. 어려운 파이썬, 알고리쥼
import sys

sys.stdin = open('./Swea/D3/1213.txt','rt',encoding='UTF8')

for tc in range(1,11):
  T = int(input())
  st = input()
  arr = input()
  # print(arr)
  cnt = arr.count(st)
  print(f'#{tc} {cnt}')
