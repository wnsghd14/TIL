import sys

sys.stdin = open('./Swea/D3/1217.txt', 'r')

T = 10
def power(a, b) :
  if b == 0 :
    return 1
  else:
    return a * power(a, b-1)

for tc in range(1,T+1):
  N = int(input())
  a, b = map(int,input().split())
  print(f"#{tc} {power(a, b)}")