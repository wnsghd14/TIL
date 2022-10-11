import sys

sys.stdin = open("_조교의성적매기기.txt")
# 아주 어려웠던 개념.각 N명의 학생들을 N개의 점수에 각각 나누어 등수를 매기는 방식
# 각 그룹 중 M번째 학생의 성적을 도출하는 것이었고 리스트 인덱스를 뽑으면 되겠구나라고 생각.
# 하지만 리스트로 접근해서 무슨 문제인지 답이 다르게 나왔고 디버깅 결과 값이 애매하게 다르게 들어간다는것을
# 알수 있었다. 하지만 이유를 못 찾겠어서 그냥 코드를 엎고 다시 짜기로 결정
# T = 10개의 조
# n = 1개의조 인원
# m = 위 중 m번째 학생
# grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
# T = int(input())
# score_list = [] # 
# for tc in range(1,T+1):
#     n,m = map(int,input().split())
    
#     for i in range(n):
#         a,b,c = map(int,input().split())
# #         score = [(a*0.35),(b*0.45),(c*0.2)]
# # # print(score)
# #         total = sum(score) 
# #         # print(total)
# #         score_list.append(total)
        
# #         result = sorted(score_list) 
#     # print(result)
#     avar = n // 10
#     student = result[m-1]
#     answer = result.index(student)//avar
#     print(f'#{tc} {grade[answer]}')
# sum 함수에서 뭐가 잘못 되었나 라고 판단하고
# 아예 더한값을 리스트에 넣어버리고
# 새로운 리스트변수를 그대로 솔팅을 하는등 방법은 같으나 조금 더 컴팩트하게 진행

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())
for tc in range(1, t + 1) :
    n, m = map(int, input().split())
    data = []
    for _ in range(n) :
        a, b, c = map(int, input().split())
        total = (a * 0.35) + (b * 0.45) + (c * 0.2)
        data.append(total)
    
    k_score = data[m-1]
    data.sort(reverse=True)
    # print(data)
    value = n // 10
    result = data.index(k_score) // value
    # print(score[result])
     # 인덱스 오류가 몇번이고 떴다 왜되었는지 이해가 잘 되질 않음.
    print(f'#{tc} {score[result]}')