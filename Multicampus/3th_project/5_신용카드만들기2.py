import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
cnt = 0
for tc in range(1,T+1):
    numbers = list(map(str,input().split()))
    for i in numbers:        
        if len(i) < 16:
            break
        if i[0] == '3' or i[0] == '4' or i[0] == '5' or i[0] == '6' or i[0] == '9':
             cnt = 1
        else:
             cnt = 0
    # print(cnt)

    print(f'#{tc} {cnt}')