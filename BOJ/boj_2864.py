import sys
input = sys.stdin.readline

N,M = input().split()

min_ = int(N.replace('6','5')) + int(M.replace('6','5'))
max_ = int(N.replace('5','6')) + int(M.replace('5','6'))
print(min_,max_)