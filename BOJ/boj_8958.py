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


T = int(input())

O = 'O'
X = 'X'

for t in range(T):
    ox = input()
    count_o = 0 # 연속된 O의 개수
    sum_ = 0 # 점수의 총합

    for answer in ox:
        if answer == O:
            count_o += 1 # 연속된 O의개수 1증가
            sum_ = count_o + sum_
        if answer == X:
            count_o = 0 # 연속된 O의 개수를 초기화
    
    print(sum_)
