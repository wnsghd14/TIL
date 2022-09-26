import sys

sys.stdin = open("./Swea/input.txt",'r')

T = int(input())

for tc in range(1,T+1):
  N = int(input())
  arr = list(map(int,input().split()))

  arr.sort() # 오름 차순 정렬
  print(f'#{tc}',end=" ")
  print(*arr) # 언패킹 연산자. 사용