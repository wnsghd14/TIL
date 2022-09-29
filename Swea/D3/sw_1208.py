# sort해서 끝값과 마지막값을 for 문에서 빼주면 된다고 생각했다.
# 이게 d3 ?!

import sys

sys.stdin = open('./Swea/D3/1208.txt','r')
for tc in range(1,11):
  T = int(input())
  arr = list(map(int,input().split()))
  for i in range(T):
    arr.sort()
    arr[0] += 1
    arr[-1] -= 1

  print(f'#{tc} {max(arr)-min(arr)}')

