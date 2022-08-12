import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
word_list =['a','e','i','o','u'] # 모음리스트

for tc in range(1,T+1):
    word = input()
    lit = [] # 
    result = '' # 출력을 위해, 초기화
    for i in word: # word 를 i 로 하면서
        if i not in word_list: # 모음안에 글자가 아닐때
            lit.append(i)
            # print(lit)
    for j in lit: # list 내부요소 뽑아서
        result += j # result 문자열모음 에다 넣어주기
        # print(j)
    print(f'#{tc} {result}')