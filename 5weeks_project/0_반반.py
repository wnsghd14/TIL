import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(1, T+1):
    word = input()
    lit1 = [] # 초기화가 필요하고 
    lit2 = [] # 인풋 문자열을 각각 비교하는게 도무지 생각이 안나서 리스트 두개에 각 값을 넣고 비교하려 함.
    clue = True # boolean 을 사용하여 비교해주기 위함.

    for i in word:
        # print(word)
        if len(lit1) == 0 : # 우선 첫번째 인덱스값을 넣어놓은 상태에서
            lit1.append(i) #
        elif i == lit1[0]: # 그 첫번째로 넣어놓은 값과 인덱스가 같다면
            lit1.append(i) # 한번더 어팬드
        elif len(lit2) == 0: # 마찬가지로
            lit2.append(i) 
        elif i == lit2[0]:
            lit2.append(i)
        else: # 만약 안된다면 True 를 False 로
            clue = False
        # print(lit1)
        # print(lit2)
    if len(lit1) != 2 or len(lit2) != 2: # 만약에 문자열 리스트 둘중 하나라도 2가 아니라면
        clue = False # No를 출력하기 위함.
    if clue == True:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')