import sys
sys.stdin = open('input.txt')
lit = []
N = int(input())
M = int(input())
for i in range(M):
    x,y = map(int,input().split())
    a = x*y
    lit.append(a)
if sum(lit) == N:
    print('Yes')
else:
    print('No')