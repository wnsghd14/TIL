import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for tc in range(1, T+1):
    num_ = list(map(int, input().split()))
    # print(num_)
    cnt = 0
    for i in range(len(num_)):
        if (i+1) % 2 == 1:
            # print(i)
            cnt += num_[i]*2
        elif (i+1) % 2 == 0:
            cnt += num_[i]
            
    # print(cnt)
    result = (100-cnt) % 10
    # print(result)
    print(f'#{tc} {result}')