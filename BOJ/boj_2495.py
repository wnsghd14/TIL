import sys
sys.stdin = open('input.txt')

# for i in range(3):
#     tem = input()
#     # 숫자를 str 으로 받는다.
#     result = 0 # 
#     for j in range(len(tem)):
#         arr = tem[j]
#     # arr 이라는 변수가 tem[j]라고 선언
#         answer = 1 # 길이변수 무조건적으로 1임.
#         for k in range(j+1,len(tem)):
#             if arr != tem[k]:# 만약 tem[j] 가 tem[k] 와 다를때 == 리스트 내부값이 연속하지 않을때
#                 break
#             if arr == tem[k]:
#                 answer += 1 # 만약 리스트 내부값이 연속할때
#         result = max(result,answer) # result에 answer의 최댓값을 넣어준다.
#     print(result)
for i in range(3):
    lit = list(input())
    lit1 = []
    k = 1 # 길이는 원래 1이니까.
    for j in range(len(lit)-1): # 인덱스오류 피하기 위해 -1 3,3 = X 3,2 = O
        if lit[j] == lit[j+1]:
            k += 1 # 1더해주고
        else:
            lit1.append(k)
            k = 1 # 아니라면 그동안의 값을 어팬드 후 초기화.
    lit1.append(k)

    print(max(lit1))