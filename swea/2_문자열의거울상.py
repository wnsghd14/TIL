import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for tc in range(1,T+1):
    words = list(input())
    result = ''
    # print(words)
    for i in range(len(words)):
        if words[::-1][i] == 'b' :
            result += 'd'
            # print(result)
        elif words[::-1][i] == 'd':
            result += 'b'
        elif words[::-1][i] == 'p':
            result += 'q'
        else:
            result += 'p'
            # print(result)
    print(f'#{tc} {result}')

