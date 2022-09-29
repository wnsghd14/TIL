import sys

sys.stdin = open('./Swea/D3/1209.txt','r')

T = int(input())

arr = [list(map(int,input().split())) for _ in range(T)]

print(arr)