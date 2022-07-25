# https://www.acmicpc.net/problem/8958
# import sys

# sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) 

for i in range(T):
    N = input() 
    total = 0
    score = 0
    for j in N: 
        if j == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)
            
