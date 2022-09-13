import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    sum_ = sum(numbers)
    average_ = sum_ / N
    result = 0
    for i in numbers:
        if i <= average_:
            result += 1
    print(f'#{tc} {result}')
