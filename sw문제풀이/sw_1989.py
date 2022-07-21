T = int(input())
for tc in range(1, T + 1):
    words = input()

    if words == words[::-1]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
    # ::-1 문자열 뒤집기를 사용하여 손쉽게 풀어 내었다.